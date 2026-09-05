import random


dices = []
dice_amount = int(input("How many dice to roll: "))

for n in range(dice_amount):
    dice = random.randint(1, 6)
    dices.append(dice)

print("Sum of the dice: " + str(sum(dices)))