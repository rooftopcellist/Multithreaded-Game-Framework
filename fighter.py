#!/usr/bin/python

import random

class Character(object):
    def name(self):
        return self._name

    def lv(self):
        return self._lv

    def hp(self):
        return self._hp

    def mp(self):
    	return self._mp

    def df(self):
    	return self._df

    def at(self):
    	return self._at

    def exp(self):
    	return self._exp

    def lv_set(self, value):
        self._lv = value

    def hp_set(self, value):
        self._hp = value

    def mp_set(self, value):
        self._mp = value

    def df_set(self, value):
        self._df = value

    def at_set(self, value):
        self._lv = value   

    def exp_set(self, value):
        self._exp = value            


class Wizard(Character):
    def __init__(self, name):
		level = 1
		self._name = name
		self._lv = level
		self._hp = 18+(2*level)
		self._mp = 10*level
		self._df = 1.8+(1.5*level)
		self._at = 3.5+(1.2*level)
		self._exp = 0

class Archer(Character):
	def __init__(self, name):
		level = 1
		self._name = name
		self._lv = level
		self._hp = 16+(2*level)
		self._mp = 10*level
		self._df = 2.2+(1.5*level)
		self._at = 3+(1.2*level)
		self._exp = 0

class Knight(Character):
	def __init__(self, name):
		level = 1
		self._name = name
		self._lv = level
		self._hp = 22+(2*level)
		self._mp = 10*level
		self._df = 4+(1.5*level)
		self._at = 2+(1.2*level)
		self._exp = 0





class Rat(Character):
    def __init__(self, level):
    	self._name = "Lesser Rat"
    	self._lv = level
        self._hp = 5
        self._mp = 0
        self._df = 2
        self._at = 5
        self._exp = random.randint(3,6)

'''

# One character attacks another. Prints out the result.
def attack(attacker, victim):
	if attacker.at() <= victim.df():
		damage = 0
	else:
		damage = attacker.at() - victim.df()

	victim.hp_set(victim.hp() - damage)
	print attacker.name(), " attacks ", victim.name()," for ", damage, " points of damage!"

# Shows HP, AT, DF, and EXP of given character.
def status(character):
	print character.name(), " has ", character.hp(), " hp, ",character.exp()," experience, " , character.at(), " attack, and ", character.df(), " defense."



def main():

	#initial enemy generation
	enemy = Rat(1)

	#title
	print "Welcome to RPG Fighter. \r\n"

	#name input
	playername = raw_input("Name your character: ")

	#generate player
	player = Wizard(1, str(playername).strip())

	print "Type 1 to attack, 2 to check status."

	# Main fighting loop
	while True:
		x = raw_input("->")

		if x is "1":
			attack(player, enemy)
			if enemy.hp() <= 0:
				print player.name(), " killed ", enemy.name(), "! "
				print player.name(), " received ", enemy.exp() ,"exp."
				player.exp_set(player.exp()+enemy.exp())
				enemy = Rat(1)
			attack(enemy, player)
			if player.hp() <= 0:
				print "GAME OVER"
				break


		elif x is "2":
			status(player)
			status(enemy)

		else:
			print "Input error. Quitting."
			break

main()
'''
