import nmap
nm=nmap.PortScanner()
nm.scan(hosts='192.168.46.145',arguments='-p-')
print(nm.csv())
print("----------------------------------")
print(nm['192.168.46.145'].tcp(22))
print(nm.command_line())
