from scapy.all import *
import sys

INTERFACE = "ens33"

def querysniff(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src 
        ip_dst = pkt[IP].dst 
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            print(str(ip_src) + " -> " + str(ip_dst) + " : " + "("+ str(pkt.getlayer(DNS).qd.qname) + ")")

sniff(iface=INTERFACE, filter="port 53", prn=querysniff, store=0)
print("[*] Shutting down...")