#!/usr/bin/python

from scapy.all import *

total = 0
for i in range(1, 255):
	ip = "192.168.40." + str(i)
	arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
	arpResponse = srp1(arpRequest, timeout=0.01, verbose=0)
	if arpResponse:
		print arpResponse.psrc
		total += 1
print "Total %s hosts alive." %total 
 


