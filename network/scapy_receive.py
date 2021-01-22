from scapy.all import *
import socket

def printer(packet):
    print("[+] got packet!")
    if packet.haslayer(Raw):
        print(packet.getlayer(Raw).load)

def sniffer():
    print("[+] Sniff started")
    while True:
        s = socket.socket()
        s.bind((SERIP, SERPORT))
        s.listen(5)
        # listen to one request
        c, addr = s.accept()
        print("Got connection from", addr)
        c.send('Thanks for connecting!')
        c.close()
        sniff(store=0, filter=FILTER, prn=printer, iface=IFACE)


if __name__ == "__main__":
    FILTER = "tcp and port 5555"
    #  "host 10.10.6.14 and port 8080"
    IFACE = "ens33"
    SERPORT = 5555
    SERIP = '' # socket can listen to any ip
    sniffer()