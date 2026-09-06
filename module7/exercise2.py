import random 

def roll_dice(sides):
    dice = random.randint(1, sides)
    return dice

sides = int(input("Enter the amount of sides: "))

while True:
    dice = roll_dice(sides)
    print(dice)
    
    if dice == sides: 
        break
