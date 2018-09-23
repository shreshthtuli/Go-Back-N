# packet.py - Packet-related functions

# Creates a packet from a sequence number and byte data
def make(seq_num, ack, data = b''):
    seq_bytes = seq_num.to_bytes(31, byteorder = 'little', signed = True)
    ack = ack.to_bytes(1, byteorder = 'little', signed = True)
    return seq_bytes + ack + data

# Creates an empty packet
def make_empty():
    return b''

# Extracts sequence number and data from a non-empty packet
def extract(packet):
    seq_num = int.from_bytes(packet[0:31], byteorder = 'little', signed = True)
    ack = int.from_bytes(packet[31:32], byteorder = 'little', signed = True)
    return seq_num, ack, packet[32:]
