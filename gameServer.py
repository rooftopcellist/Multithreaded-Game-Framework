"""
Program: FINAL PROJECT GAME
Authors: Christian Adams, Steve Myrick, Jeff Kidwell, Ethan Ingalls
 
"""

#!/usr/bin/python
from socket import *
from time import ctime
import time
from threading import Thread
from gameLog import GameLog
from gameLogic import gameLogic

global clientList
clientList = []

class ClientHandler(Thread):
	#Manages client requests
	def __init__(self, client, record):
		Thread.__init__(self, name = "")
		self._client = client
		clientList.append(client)
		self._record = record
		
		
	def run(self):
		self._client.send(ctime() + '\nWelcome to the Game.')
		self._name = self._client.recv(BUFSIZE)
		self._class = self._client.recv(BUFSIZE)
		game.makeCharacter(self._name, self._class)								#makes character in gameLogic using Character class from fighter.py
		#self._client.send(str(self._record))
		reply = '{0} is a {1}' .format(self._name, self._class)
		self._client.send(str(reply))
		while True:
			message = self._client.recv(BUFSIZE)
			if not message:
				print "Client Disconnected"
				self._client.close()
				break
			else:
				reply = game.logic(message)
				#reply = message								#<<<Unhash this line to bypass gameLogic and forward client messages instead.
				reply = '{0}: {1}'.format(self._name, reply)
				self._record.add(reply)
				for item in clientList:
					item.send(str(self._record))
				#self._client.send(str(self._record))          #<<<This line of code will send only to the client it received from
				
				''' If you want to send to a specific client, just index it: clientList[0].send(str(self._record))'''
				



HOST = 'localhost'
PORT = 1234
ADDRESS = (HOST, PORT)
BUFSIZE = 1024

game = gameLogic()
record = GameLog()
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDRESS)
s.listen(5)

while True:
	print 'Waiting for connection...'
	client, address = s.accept()
	print'... accepted connection from:', address
	handler = ClientHandler(client, record)
	handler.start()
	

