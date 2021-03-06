#!/usr/bin/env python3
  
from scapy.all import *
import time

src_ports = [2000, 2001, 2004, 2005, 2003, 3003]
fin_src_ports = [10000, 20000, 30000, 40000, 50000]

packet_generator = IP(ttl=10, dst="10.2.10.2")/UDP(sport=src_ports, dport=5500)
fin_packet       = IP(ttl=10, dst="10.2.10.2")/UDP(sport=fin_src_ports, dport=5500)

info = [
        ("source", packet_generator.src),
        ("source ports", packet_generator.sport),
        ("destination", packet_generator.dst),
        ("destination ports", packet_generator.dport),
        ("fin source ports", fin_packet.sport),
        ("fin destination ports", fin_packet.dport)
    ]

print( "packet_generator:" )

for dat in info:
    print( "%40s\t%40s" % (dat[0], dat[1]) )

while True:
    for ii in range(1000):
        send(packet_generator, verbose=False)
    send(fin_packet, verbose=False)
    time.sleep(10)
