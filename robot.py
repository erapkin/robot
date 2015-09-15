import random

class Robot (object):
	
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
	
class JuggernautRobot(Robot):

	def punch(self, amount=5):
		super(JuggernautRobot, self).punch(amount)
		
	
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
			




