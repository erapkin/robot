import random

class Robot :
	
	def __init__(self, powerSupply):
		self.powerSupply = powerSupply
		
		
	def punch(self, amount=3):
		punchList = ['Doing the Robot on yo face', 'Jackie Chan Strike', '"what is that?" punches face', 'Uppercut', 'B@#$Slap','WubWubWubWubWub', 'Moonwalk all over then STRIKE']
		
		print self.powerSupply.powerBalance
		if  (self.powerSupply.powerBalance > 2):
			self.powerSupply.drain(amount)
			print (random.choice(punchList))
		else:
			print "Insufficient power to punch"
			exit(0)
			
	def multiplePunch(self, numberOfPunches):
		for x in range (0,numberOfPunches):
			self.punch()	
	
	# def chargedrain():

class LaserRobot(Robot):

	def shootLaser(self,amount):
		self.powerSupply.drain(amount)
		print "Pew Pew"

class NinjaRobot(Robot):
	
	def slice(self,amount):
		self.powerSupply.drain(amount)

		
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
		
duracelBattery = RechargableBattery(100)
# energizerBattery = RechargableBattery(100)
shinobi = Robot(duracelBattery)

number = raw_input('How many punches?:')
shinobi.punch()
shinobi.multiplePunch(int(number))

print "======================================="
print "current power balance: "
duracelBattery.printPowerBalance()




# duracelBattery.drain (5)
# duracelBattery.charge (15)

