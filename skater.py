from funcs import *
def main():
	pounds = input("How much do you weigh (pounds)? " )
	distance = input("How far away is your professor (meters)? ")
	object = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")
	print()
	massSkater = poundsToKG(pounds)
	mass = getMassObject(object)
	VelocityObject = getVelocityObject(distance)
	VelSkater = getVelocitySkater(massSkater, mass, VelocityObject)
	
	#convert distance to an int
	distance = int(distance)

	if mass <= 0.1:
		print("Nice throw! You're going to get an F!")
	elif mass > 0.1 and mass <=1.0:
		print("Nice throw! Make sure your professor is OK.")
	elif mass > 1.0:
		if distance < 20:
			print("Nice throw! How far away is the hospital?")
		elif distance >= 20:
			print("Nice throw! RIP professor.")
	print("Velocity of skater: " + "%.3f" %VelSkater + " m/s") 	
	if VelSkater < 0.2:
		print("My grandmother skates faster than you!")
	elif VelSkater >= 1.0:
		print("Look out for that railing!!!")	
if __name__ == '__main__':
	main()
