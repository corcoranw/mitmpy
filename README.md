# mitmpy
python man in the middle

### I am not responsible for unlawful use of this code

## Demo <br>



https://github.com/corcoranw/mitmpy/assets/128327923/5e71d91d-7b4c-4a0e-b407-31f878eb9560




## Pseudocode<br>
### main<br>
Get arguments<br>
Check arguments<br>
set victim<br>
set gateway<br>
set interface<br>
set website<br>
launch arpspoof in its own thread<br>
launch sniff<br><br>

### arpspoof<br>
thread loop sending arp responses to victim<br>
thread loop sending arp responses to gateway<br><br>

### sniff<br>
open interface<br>
capture traffic using filter for victim dns packets<br>
when match, launch dnsspoof function<br><br>

### dnsspoof<br>
decode dns packets to extract website domain name<br>
create dns response with website domain name<br>
send spoof dns to victim<br>
print sent packet<br><br>

## Usage<br>
run<br>
sudo ./arpspoof.py<br>
and<br>
sudo ./main.py <interface> <ip-victim> <ip-website><br>
interface=interface to sniff on and to send dns through<br>
ip-victim=the ip address of the victim machine<br>
ip-website=the ip address of the website to redirect dns to<br>
example:<br>
sudo ./main.py eth0 192.168.1.84 192.168.1.82<br>

