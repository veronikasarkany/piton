beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]

counter = 0
nyiregyJut = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Nyíregyháza"):
		nyiregyJut += float (lineSpt [4])
		counter += 1

atl = nyiregyJut / counter	
print ("Nyíregyházi jutalom átlag:", atl)	
	
