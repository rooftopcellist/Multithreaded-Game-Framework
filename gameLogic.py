#!/usr/bin/python

import random
from fighter import Character, Wizard, Archer, Knight



class gameLogic(object):
	def __init__(self):
		self.playerList = []						#This is a list of all the player objects created and appended in makeCharacter
		
	def makeCharacter(self, name, class_choice):
		if class_choice == 'Wizard':
			newCharacter = Wizard(name)
			self.playerList.append(newCharacter)
		elif class_choice == 'Archer':
			newCharacter = Archer(name)
			self.playerList.append(newCharacter)
		elif class_choice == 'Knight':
			newCharacter = Knight(name)
			self.playerList.append(newCharacter)
			print self.playerList

	def respond(self, s):
		m = "This is the response"
		#m = self.response
		return "This is the response"
		
	def logic(self, _input):						#This function could contain the main game logic
		pass
		m = "output to clients "					#Acts as a send all to every client connected
		return m
		