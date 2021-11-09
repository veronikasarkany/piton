def getData ():
	
	side = float (input("oldala:"))
	return side

def control(sides):
	
	if (sides[0] + sides[1] > sides[2]) and (sides[0]) + sides[2] > sides[1] and (sides[1]) + sides[2] > sides[0]:
		return True
	else:
		return False

def calculate( sides):
	
	ker = sides[0] + sides[1] + sides[2]
	print ("A háromszög kerülete:", ker)

def start():
	
	sides = []
	
	for i in range (0,3):
		sides.append (getData())
		
	check = control (sides)
	if check:
		calculate(sides)
		
	else:
		print ("Nem háromszög")


	
start()

