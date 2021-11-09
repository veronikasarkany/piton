def getData ():
	
	side = float (input("oldala:"))
	return side

def control(sides):
	
	if (sides[0] + sides[1] > sides[2]) and (sides[0]) + sides[2] > sides[1] and (sides[1]) + sides[2] > sides[0]:
		return True
	else:
		return False

def start():
	
	sides = []
	
	for i in range (0,3):
		sides.append (getData())
		
	check = control (sides)


	
start()

