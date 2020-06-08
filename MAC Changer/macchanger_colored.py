import subprocess
from termcolor import *


interface=input("Which interface would you like change it's MAC address? :")
new_mac_address = input("Enter the new MAC: ")

before_change = subprocess.check_output(["ifconfig",interface])
#print(before_change)

subprocess.call(["ifconfig",interface,"hw","ether",new_mac_address])
after_change = subprocess.check_output(["ifconfig",interface])
#print(after_change)

if before_change == after_change:
    print(colored("failed to change MAC address to " + new_mac_address,'red'))
else:
    print(colored("Mac address changed to %s successfull " %new_mac_address, 'green'))

