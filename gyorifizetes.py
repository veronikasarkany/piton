beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]
gyorFizu = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Győr"):
		gyorFizu += float (lineSpt [3]) 

	
print ("Győriek fizetése:", gyorFizu)	
	
