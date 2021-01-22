from scapy.all import *

send(IP(dst='8.8.8.8')/TCP(dport=53, flags='S'), count=10)