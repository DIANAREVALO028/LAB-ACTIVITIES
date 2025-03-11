def classify_age(age):
	if age < 0:
		print("invalid age, Please enter a positive number.")
	elif age <=12:
		print("You are a Child.")
	elif age<=19:
		print("You are a Teen.")
	elif age <=54:
		print("You are a Adult.")
	else:
		print("You are a Senior.")
		
while True:
	age = int(input("Enter your age."))
	classify_age(age)