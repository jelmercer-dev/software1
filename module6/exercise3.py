integer = int(input("Enter an integer: "))

prime = integer >= 2

for divisor in range(2, int(integer ** 0.5) + 1):
	if integer % divisor == 0:
		prime = False
		break

if prime:
	print(f"{integer} is a prime number.")
else:
	print(f"{integer} is not a prime number.")
