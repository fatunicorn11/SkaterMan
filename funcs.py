#Convert pounds to kilograms
#str -> int
def poundsToKG(pounds):
	pounds = int(pounds)
	kilograms = pounds * 0.453592
	return kilograms
#Take user input to find mass of object
#str -> int	
def getMassObject(object):
	if object == "t":
		mass = 0.1
	elif object == "p":
		mass = 1.0
	elif object == "r":
		mass = 3.0
	elif object == "g":
		mass = 5.3
	elif object == "l":
		mass = 9.07
	else:
		mass = 0.0
	return mass
#Take user input to find velocity
#str -> int
def getVelocityObject(distance):
	distance = int(distance)
	VelocityObject = (((9.8 * distance) / 2) ** 0.5)
	return VelocityObject	
#Find velocity of skater
#int, int, int -> int
def getVelocitySkater(massSkater, massObject,VelocityObject):
	velocitySkater = (massObject * VelocityObject)/(massSkater)
	return velocitySkater 
