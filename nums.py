from datetime import datetime

i = input('What is the number? ')
name = 'myname'



day = datetime.now().day

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
		if (val == day):
			i2 = input("Enter 3 more numbers seperated by commas. Ex: 5,9,12: ")
			var2 = i2.split(',')
			print(var2)
			# var2 is an array containing 3 strings
			

			## get result here
			result = 5
			if (result < 0):
				print(result)
			elif (result == 0):
				print(name)
			else:
				print("-"*result)

		break



	except ValueError:
		print("Not a number")
