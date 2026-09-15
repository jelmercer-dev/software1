import random

points = int(input("How many random points should be generated? "))

counter = 0
circle = 0


while counter < points:

	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)

	if x ** 2 + y ** 2 < 1:
		circle += 1

	counter += 1

pi = 4 * circle / points
print("Approximation of pi:", pi)