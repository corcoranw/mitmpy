#!/usr/bin/python
from sniff import *
import sys
import time
import os

os.system("iptables -A FORWARD -p udp --sport 53 -d " + sys.argv[2] + " -j DROP")
os.system("iptables -A FORWARD -p tcp --sport 53 -d " + sys.argv[2] + " -j DROP")

time.sleep(2)

print("starting sniff")
snuffle(sys.argv[1], sys.argv[2], sys.argv[3])
