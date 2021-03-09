from scapy.all import *
import socket

try:
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #send(IP(dst=”< IP-Address-of-Destination”)/<Protocol>/”Message”)
    p = IP(dst="10.10.6.14")/TCP(flags="S", sport=RandShort(),dport=8080)/"Hallo world!"
    # s.connect(("10.10.6.14",5555))
    # s.send(bytes(p))
    sendp(p)
    
    print("[+] Request Sent!")
except Exception as e:
    raise e