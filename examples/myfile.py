class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

dog = Dog("Bubbles", 2022)
dog1 = Dog("Waxz", 2076)

print(f"{dog.name:s} was born in {dog.birth_year:d}.")
print(f"{dog1.name:s} was born in {dog1.birth_year:d}.")
