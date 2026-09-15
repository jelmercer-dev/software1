import random

number = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))

while guess != number:

    if guess < number:
        print("Too low")
    if guess > number:
        print("Too high")

    guess = int(input("Guess a number (1-10): "))
    
if guess == number:
    print("Correct")