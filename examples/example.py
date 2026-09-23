class Potion:
    def __init__(self, name):
        self.name = name

class HealthPotion(Potion):
    def __init__(self, name, hp):
        super().__init__(name)
        self.hp = hp

class Poison(Potion):
    def __init__(self, name, hp, amount):
        Potion.__init__(name)
        self.hp = hp
        self.amount = amount
#Main program
potion = HealthPotion("Health Potion",2)
print(f"{potion.name}: + {potion.hp}")
poison = Poison("Orc Slayer", 5, 3)
print(f"{poison.name}: - {poison.hp}, remaining: {poison.amount}")