import scapy.all as scapy

print("default arp packet")
arpRequest = scapy.ARP()
print(arpRequest.show())

print(arpRequest.summary())

print("Sending a broadcast packet.")

arpR = scapy.ARP(pdst= '127.0.0.1')
# To make sure that our request will be sent to all devices in the network, we need to set the broadcast MAC address.
broadcastP = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

arpReqBroad = broadcastP/arpRequest

answ, unansw = scapy.srp(arpReqBroad, timeout=1)

print(answ.summary())
print(unansw.summary())

print("Finding address of all the computers in the network.")
arpAll = scapy.ARP(pdst='192.168.0.0/24') 

print(arpAll.show())