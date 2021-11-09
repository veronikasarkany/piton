class Alien:
	
	legs = 5
	heName = ""
	
	def __init__(self,beName ):
		
		self.heName = beName

alien01 = Alien("Brandon")
print (alien01.heName, alien01.legs)

alien02 = Alien ("Maven")
alien02.legs = 9
print (alien02.heName, alien02.legs)
