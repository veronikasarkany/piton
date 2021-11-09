"""
{(28/2)+40}/4
"""

def subtract():
	result = 28 / 2
	return result 

def divide(num01):
	
	result = num01 + 40
	return result

def multiply (num02):
	
	result = num02 / 4
	return result	

def out(num03):
	
	print ("Az eredmény:" ,num03)
	

def start():
	print ("Gyártó: Saját Név")
	
	num01 = subtract()
	num02 = divide (num01)
	num03 = multiply (num02)
	out (num03)

start()
