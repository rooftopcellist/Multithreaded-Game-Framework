#!/usr/bin/python

from socket import *
from threading import Thread
import random, time

class createThread1(Thread):
	def __init__(self):
		Thread.__init__(self)
	
	def run(self):
		self.sendLoop()
		
	def sendLoop(self):
		#print "here in send loop"
		while True:
			message = raw_input('')
			if not message:
				print 'Server disconnected'
				break
			s.send(message + '\n')
			time.sleep(.01)
		s.close()


class createThread2(Thread):
	def __init__(self):
		Thread.__init__(self)
	
	def run(self):
		self.recvLoop()
		
	def recvLoop(self):
		#print "here in recv loop"
		while True:
			record = s.recv(BUFSIZE)
			if not record:
				print 'Server disconnected'
				break
			print record
		s.close()


HOST = 'localhost'
PORT = 1234
BUFSIZE = (1024)
ADDRESS = (HOST, PORT)


s = socket(AF_INET, SOCK_STREAM)   # Specifies the family and type of connection (TCP) of the socket & assigns it to 's'
s.connect(ADDRESS)          		# Connections to Server through port 1234 on the localhost (127.0.0.1)

print s.recv(BUFSIZE)			#prints server's greeting
name = raw_input('Enter your name: ')
s.send(name)
while True:
	class_name = raw_input('Enter [1] to be a Wizard, [2] to be an Archer, or [3] to be a Knight\n')
	class_choice = '0'
	if class_name == '1':
		class_choice = 'Wizard'
		break
	elif class_name == '2':
		class_choice = 'Archer'
		break
	elif class_name == '3':
		class_choice = 'Knight'
		break
	else:
		print "That is not a valid input, try again."
s.send(class_choice)


sys = createThread2()
sys.start()

sys = createThread1()
sys.start()

