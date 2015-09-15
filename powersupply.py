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