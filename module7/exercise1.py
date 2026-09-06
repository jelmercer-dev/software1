import random 

def roll_dice():
    dice = random.randint(1, 6)
    return dice


while True:
    dice = roll_dice()
    print(dice)
    
    if dice == 6: 
        break
