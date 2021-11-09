beFajl = open( "feherBt.txt", "r",encoding="utf-8")


counter = 0
row = beFajl.readline()
while(row):
	
	
	row = beFajl.readline()
	if (row != ""):
		counter +=1
	
	
print("Dolgozók szám:", counter)
