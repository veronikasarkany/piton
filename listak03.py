list01 = []
list02 = [2,4,3,6,7]

print (list01)
print (list02)

list01.append ( 10 )
list01.append ( 11 )
list01.append ( 12 )
list01.append ( True )

print (list01)

list01.insert ( 1, "szo" )
list01.insert ( 3, "másik szo")

print (list01)

for listElement in list01:
	if type (listElement)  == str:
		print ( listElement )

print (list01)
del (list01[3])

print (list01)

for listElement in list01:
	print ( listElement )
