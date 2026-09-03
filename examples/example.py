names = []

name = input("Enter the first name or quit by pressing Enter: ")

while name != "":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

for n in names:
    print(f"Hello, {n}!")