import socket
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def port_is_open(host, port):

	s=socket.socket()
	try:
		s.connect((host,port))
	except:
		return False

	else:
		return True

host = input("Enter the IP address:")

for port in range(1,800):

	if port_is_open(host,port):
		print(f"{GREEN}[+] {host}:{port} is open	{RESET}")
	else:
		print(f"{GRAY}[!] {host}:{port} is closed	{RESET}", end="\r")
