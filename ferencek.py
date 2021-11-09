beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]

counter = 0

for line in row:
	
	lineSpt = line.split(":")
	lineSpt02 = lineSpt[0].split(" ")
	if (lineSpt02[1] == "Ferenc"):
		
		counter += 1


print("Ferenc:", counter)
	

