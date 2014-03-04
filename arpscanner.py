#!/usr/bin/python

from scapy.all import *



a = IP(dst="8.8.8.8")
ip = a.src
print "local ip is %s" %ip
subnet = ip[:ip.rfind(".")+1]

total = 0
for i in range(1, 255):
	ip = subnet + str(i)
	arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
	arpResponse = srp1(arpRequest, timeout=0.01, verbose=0)
	if arpResponse:
		print arpResponse.psrc
		total += 1
print "Total %s hosts alive." %total 
 


