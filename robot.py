import random

class Menu:
	def pickRobot (self):

		print "Which robot do you want to choose?"
		print "1)Wraith, 2)Hell Knight 3)Juggernaut"
		running = True
		while running:	
			try:
				robotPick = (int)(raw_input())
				if (robotPick == 1):
					print "You picked Wraith"
					running = False
				elif (robotPick ==2):
					print "You picked Hell Knight"
					running = False
				elif (robotPick ==3):
					print "You picked Juggernaut"
					running = False
				else:
					print "Wrong number selection, try again\n"
					running = True
			except Exception:
				print "------------------------------------------------------------"
				print "\nIncorrect input. Please select a number from the menu.\n"
				running = True

		
class Robot :
	
	def __init__(self, powerSupply):
		self.powerSupply = powerSupply
		
		
	def punch(self, amount=3):
		punchList = ['Doing the Robot on yo face', 'Jackie Chan Strike', '"what is that?" punches face', 'Uppercut', 'B@#$Slap','WubWubWubWubWub', 'Moonwalk all over then STRIKE']
		
		if  (self.powerSupply.powerBalance > 2):
			self.powerSupply.drain(amount)
			print (random.choice(punchList))
			print (str(self.powerSupply.powerBalance) + " power point" + "(s) " + "remaining\n")
		else:
			print "Insufficient power to punch"
			exit(0)
			
	def multiplePunch(self, numberOfPunches):
		for x in range (0,numberOfPunches):
			self.punch()	
	
	# def chargedrain():

class JuggernautRobot(Robot):
	
	def earthquake(self, amount=3):
		punchList = ['HULK SMASH', 'Prepare for death', 'Im a Brick House', 'What is your mom doing later', 'Ugnnnngggggghghhhhghhhhhhh']
		
		if (self.powerSupply.powerBalance > 4):
			self.powerSupply.drain(amount)
			print (random.choice(punchList))
			print (str(self.powerSupply.powerBalance) + " power point" + "(s) " + "remaining\n")
		else:
			print "Battery Power Depleted"

class WraithRobot(Robot):
	
	def manipulateAether(self,amount):
		punchList = ['I see you', 'Turn around and DIEEEE!!', 'I AM OMNISCIENCE', 'The dark lord calls you', 'Casper is my cousin twice removed']
		
		if (self.powerSupply.powerBalance > 4):
			self.powerSupply.drain(amount)
			print (random.choice(punchList))
			print (str(self.powerSupply.powerBalance) + " power point" + "(s) " + "remaining\n")
		else:
			print "Battery Power Depleted"

class ShinobiRobot(Robot):

	def teleportSlash(self,amount):
		self.powerSupply.drain(amount)
		punchList = []

class HellKnightRobot(Robot):

	def	doomLance(self,amount):
		punchList = ['For glory and dishonor.', 'Reaping souls since 2015', 'My fury engulfs all', 'Deaths grasp is infinite', 'I give no quarter']
		
		if (self.powerSupply.powerBalance > 4):
			self.powerSupply.drain(amount)
			print (random.choice(punchList))
			print (str(self.powerSupply.powerBalance) + " power point" + "(s) " + "remaining\n")
		else:
			print "Battery Power Depleted"
			
class PowerSupply :
		
	def __init__ (self, powerBalance):
		self.powerBalance = powerBalance
		
	def drain (self, amount):
		if (self.powerBalance > 0):
			self.powerBalance -= amount
		else:
			print "insufficient power"
		
	def printPowerBalance (self):
		print self.powerBalance 
	
class RechargableBattery(PowerSupply):
			
	def charge (self, amount):
		self.powerBalance += amount
		
menu = Menu()
menu.pickRobot()

number = raw_input('How many punches?:')
juggernaut.multiplePunch(int(number))
print "======================================="
print "current power balance: "
duracelBattery.printPowerBalance()





