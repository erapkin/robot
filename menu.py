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
