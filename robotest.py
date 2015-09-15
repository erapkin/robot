import random
from robot import *
from menu import *
from powersupply import *

class Test:
	def testWraithRobot(self):
		duracelBattery = RechargableBattery(100)
		wraith = WraithRobot(duracelBattery)
		menu = Menu ()
		menu.pickRobot()
		number = raw_input("How many punches?")
		wraith.multiplePunch(int(number))
		
	def testJuggernautRobot(self):
		duracelBattery = RechargableBattery(100)
		juggernaught = JuggernautRobot(duracelBattery)
		number = raw_input("How many punches?")
		juggernaught.multiplePunch(int(number))
		
	def testMenu (self):
		menu = Menu()
		menu.pickRobot()
		
test1 = Test()
test1.testMenu()
# test1.testJuggernautRobot()


	