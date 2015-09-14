class Robot :
	
	def __init__(self, powerSupply):
		self.powerSupply = powerSupply
		
	def punch(self, amount):
		self.powerSupply.drain(amount)
		print "You punch. Kapow!"
		
	# def drainOpponent():

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
		self.powerBalance -= amount
		
	def printPowerBalance (self):
		print self.powerBalance 
	
class RechargableBattery(PowerSupply):
			
	def charge (self, amount):
		self.powerBalance += amount
		

			
duracelBattery = RechargableBattery(100)
energizerBattery = RechargableBattery(100)
shinobi = Robot(duracelBattery)

shinobi.punch(5)
duracelBattery.printPowerBalance()
shinobi.punch(4)
duracelBattery.printPowerBalance()

# duracelBattery.drain (5)
# duracelBattery.charge (15)

