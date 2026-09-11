names = set()
name = str(input())

while name != "":

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

    name = input()


print(names)