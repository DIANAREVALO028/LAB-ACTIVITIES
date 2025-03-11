def check_number(num):
	if num % 2 == 0:
		print(f"{num} is an Even number.")
	else:
		print(f"{num} is an Odd number.")
		
while True:
	num = int(input("Enter your number:"))
	check_number(num)