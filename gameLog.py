#!/usr/bin/python

class GameLog(object):
	
	def __init__(self):
		self.data = ''
		
	def add(self, s):
		self.data = s
		
	def __str__(self):
		if self.data == '':
			return 'EMPTY.'
		else:
			
			return self.data
	
	
	
	'''
	def __init__(self):
		self.data = []
		
	def add(self, s):
		self.data.append(s)
		
	def __str__(self):
		if len(self.data) == 0:
			return 'EMPTY.'
		else:
			return '\n'.join(self.data)
	'''