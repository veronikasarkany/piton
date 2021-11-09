beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]
miskolciak = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Miskolc"):
		miskolciak += 1

	
print ("Miskolci dolgozók:", miskolciak)	
	
