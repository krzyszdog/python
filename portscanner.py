import random
from scapy.all import *
from scapy.layers.inet import IP, TCP

target = input("Enter target IP address: ")

for dst_port in range(0, 100):
    src_port = random.randint(1024, 6553)
    syn_packet = sr1(IP(dst=target) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)
    if syn_packet is not None:
        if syn_packet.haslayer(TCP):
            if syn_packet.getlayer(TCP).flags == 0x12:
                print(f"Port {dst_port} is open")
                rst_packet = sr(IP(dst=target) / TCP(sport=src_port, dport=dst_port, flags="R"), timeout=1, verbose=0)