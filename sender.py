# sender.py - The sender in the reliable data transfer protocol
import packet
import socket
import sys
import _thread
import time
import udt

from timer import Timer

PACKET_SIZE = 512
RECEIVER_ADDR = ('localhost', 8080)
SENDER_ADDR = ('localhost', 0)
SLEEP_INTERVAL = 0.05
TIMEOUT_INTERVAL = 0.5
WINDOW_SIZE = 4

# Shared resources across threads
base = 0
mutex = _thread.allocate_lock()
send_timer = Timer(TIMEOUT_INTERVAL)

# Sets the window size
def set_window_size(num_packets):
    global base
    return min(WINDOW_SIZE, num_packets - base)

# Send thread
def send(sock, filename):
    global mutex
    global base
    global send_timer

    # Open the file
    try:
        file = open(filename, 'rb')
    except IOError:
        print('Unable to open', filename)
        return
    
    # Add all the packets to the buffer
    packets = []
    seq_num = 0
    while True:
        data = file.read(PACKET_SIZE)
        if not data:
            break
        packets.append(packet.make(seq_num, 0, data))
        seq_num += 1

    num_packets = len(packets)
    print('I gots', num_packets)
    window_size = set_window_size(num_packets)
    next_to_send = 0
    base = 0

    # Start the receiver thread
    _thread.start_new_thread(receive, (sock,))

    while base < num_packets:
        mutex.acquire()
        # Send all the packets in the window
        while next_to_send < base + window_size:
            print('Sending packet', next_to_send)
            udt.send(packets[next_to_send], sock, RECEIVER_ADDR)
            next_to_send += 1

        # Start the timer
        if not send_timer.running():
            print('Starting timer')
            send_timer.start()

        # Wait until a timer goes off or we get an ACK
        while send_timer.running() and not send_timer.timeout():
            mutex.release()
            print('Sleeping')
            time.sleep(SLEEP_INTERVAL)
            mutex.acquire()

        if send_timer.timeout():
            # Looks like we timed out
            print('Timeout')
            send_timer.stop();
            next_to_send = base
        else:
            print('Shifting window')
            window_size = set_window_size(num_packets)
        mutex.release()

    # Send empty packet as sentinel
    udt.send(packet.make_empty(), sock, RECEIVER_ADDR)
    file.close()
    
# Receive thread
def receive(sock):
    global mutex
    global base
    global send_timer

    try:
        file = open(writefilename, 'wb')
    except IOError:
        print('Unable to open', writefilename)
        return

    expected_num = 0
    while True:
        pkt, _ = udt.recv(sock);
        seq_num, ack, data = packet.extract(pkt)

        # If we get an ACK for the first in-flight packet
        if(ack >= 1):
            print('Got ACK', seq_num)
            if (seq_num >= base):
                mutex.acquire()
                base = ack + 1
                print('Base updated', base)
                send_timer.stop()
                mutex.release()

        else:
            print('Gor DATA', seq_num)
            if seq_num == expected_num:
                print('Got expected packet')
                print('Sending ACK', expected_num)
                pkt = packet.make(expected_num, 1)
                udt.send(pkt, sock, addr)
                expected_num += 1
                file.write(data)
            else:
                print('Sending ACK', expected_num - 1)
                pkt = packet.make(expected_num - 1, 1)
                udt.send(pkt, sock, addr)


# Main function
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Expected filename as command line argument')
        exit()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(SENDER_ADDR)
    filename = sys.argv[1]
    writefilename = sys.argv[2]

    send(sock, filename)
    sock.close()