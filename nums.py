from datetime import datetime

i = input('What is the number?')



month = datetime.now().month

while True:
	try:
		val = int(i)
		if (val == 0):
			print("Thank you")

		elif ((val < 10 and val > 0) or (val > -10 and val < 0)):
			if (val > 0):
				print("One digit number is postive")
			else:
				print("One digit number is negative")		
		else: 
			if (val < 100 and val > 9):
				print("Two digit positive number")
				if (val == month):
					i2 = input("Enter 3 more numbers: ")
					# Do the range stuff
		break



	except ValueError:
		print("Not a number")
