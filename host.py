'''

Host file for sending and receiving data using Go Back N protocol
Authors:
    - Shreshth Tuli
    - Samarth Aggarwal

Usage-
    python3 host.py 0_or_1 window_size file_to_send file_to_write
    
'''
import packet
import socket
import sys
import _thread
import time
import udt
import random

from timer import Timer

PACKET_SIZE = 1
SLEEP_INTERVAL = 0.05
TIMEOUT_INTERVAL = 0.1
WINDOW_SIZE = 7
timeouts = 0
loss = 0

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
        PACKET_SIZE = random.randint(32, 221)
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
    global timeouts
    timeouts = 0

    while base < num_packets:
        mutex.acquire()
        # Send all the packets in the window
        while next_to_send < base + window_size:
            print('Sending packet', next_to_send)
            print('Sending to ', RECEIVER_ADDR)
            udt.send(packets[next_to_send], sock, RECEIVER_ADDR, loss)
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
            timeouts = timeouts + 1
            print('Timeout', timeouts)
            send_timer.stop();
            next_to_send = base
        else:
            print('Shifting window')
            print('Number of Timeouts', timeouts)
            window_size = set_window_size(num_packets)
        mutex.release()

    # Send empty packet as sentinel
    udt.send(packet.make_empty(), sock, RECEIVER_ADDR, loss)
    file.close()
    
# Receive thread
def receive(sock):
    global mutex
    global base
    global send_timer
    global timeouts

    try:
        file = open(writefilename, 'wb')
    except IOError:
        print('Unable to open', writefilename)
        return

    expected_num = 0
    while True:
        pkt, addr = udt.recv(sock);
        seq_num, ack, data = packet.extract(pkt)

        print('Got packet with address = ',addr)

        # If we get an ACK for the first in-flight packet
        if(len(pkt) == 0):
            print('Number of Timeouts', timeouts)
            print('Last got ack', expected_num-1)
            sys.exit(0)
        if(seq_num == 1):
            timeouts = 0
        if(ack >= 1):
            print('Got ACK', seq_num)
            if (seq_num >= base):
                mutex.acquire()
                base = seq_num + 1
                print('Base updated', base)
                send_timer.stop()
                mutex.release()

        else:
            print('Got DATA', seq_num)
            if seq_num == expected_num:
                mutex.acquire()
                print('Got expected packet')
                print('Count : ', expected_num)
                print('Sending ACK', expected_num)
                pkt = packet.make(expected_num, 1)
                udt.send(pkt, sock, addr, loss)
                expected_num += 1
                file.write(data)
                mutex.release()
            else:
                mutex.acquire()
                print('Did not get expected packet', expected_num)
                print('Sending ACK', expected_num - 1)
                pkt = packet.make(expected_num - 1, 1)
                udt.send(pkt, sock, addr, loss)
                mutex.release()


# Main function
if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    RECEIVER_ADDR = ('localhost', 8080)
    SENDER_ADDR = ('localhost', 1200)
    if(sys.argv[1] == '1'):
        RECEIVER_ADDR = ('localhost', 1200)
        SENDER_ADDR = ('localhost', 8080)

    WINDOW_SIZE = int(sys.argv[2])
    
    print(SENDER_ADDR);
    sock.bind(SENDER_ADDR)

    filename = sys.argv[3]
    writefilename = sys.argv[4]
    loss = int(sys.argv[5])
    
    send(sock, filename)
    sock.close()
