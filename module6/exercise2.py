numbers = []

while True:
    value = input("Enter a number: ")

    if value == "":
        break

    value = float(value)
    numbers.append((value))

numbers.sort(reverse=True)

print(f"The greatest numbers in descending order: ")

for number in numbers[:5]:
    print(number)