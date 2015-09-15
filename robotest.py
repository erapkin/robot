import robot

class Test:
	def testWraithRobot(self):
		duracelBattery = RechargableBattery(100)
		wraith = WraithRobot(duracelBattery)
		wraith.manipulateAether(10)
		