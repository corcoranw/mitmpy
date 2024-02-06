# mitmpy
python man in the middle

### I am not responsible for unlawful use of this code

Pseudocode
main
Get arguments
Check arguments
set victim
set gateway
set interface
set website
launch arpspoof in its own thread
launch sniff

arpspoof
thread loop sending arp responses to victim
thread loop sending arp responses to gateway

sniff
open interface
capture traffic using filter for victim dns packets
when match, launch dnsspoof function

dnsspoof
decode dns packets to extract website domain name
create dns response with website domain name
send spoof dns to victim
print sent packet

Usage
run
sudo ./arpspoof.py
and
sudo ./main.py <interface> <ip-victim> <ip-website>
interface=interface to sniff on and to send dns through
ip-victim=the ip address of the victim machine
ip-website=the ip address of the website to redirect dns to
example:
sudo ./main.py eth0 192.168.1.84 192.168.1.82

