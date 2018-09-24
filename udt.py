# udt.py - Unreliable data transfer using UDP
import socket
import random

# Send a packet across the unreliable channel
# Packet may be lost
def send(packet, sock, addr):
    a = random.randint(1,100)
    loss = 95
    if(a<loss):
        return
    else:
        sock.sendto(packet, addr)
    return

# Receive a packet from the unreliable channel
def recv(sock):
    packet, addr = sock.recvfrom(1024)
    return packet, addr
