beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]

counter = 0
bpFizu = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Budapest"):
		bpFizu += float (lineSpt [3])
		counter += 1

atl = bpFizu / counter	
beFajl.close()

kiFajl = open( "budapest.txt", "w", encoding="utf-8")
kiFajl.write( "Bp fizu atlag: ")
kiFajl.write("\n")	
kiFajl.write( str (atl))
kiFajl.close()
print("Kész")
