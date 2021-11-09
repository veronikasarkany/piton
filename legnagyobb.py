num01Str = input("szám 1: ")
num01 = int(num01Str)

num02 = int(input("Szám 2:"))
num03 = int(input("Szám 3:"))

maxNum = num01

if maxNum < num02:
	maxNum = num02
	
if maxNum < num03:
	maxNum = num03 
	
print (maxNum)
