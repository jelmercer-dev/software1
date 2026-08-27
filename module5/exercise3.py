
numbers = []

number = input("Enter a number (or press Enter to quit): ")

while number != "":
    numbers.append(float(number))
    number = input("Enter a number (or press Enter to quit): ")

if numbers: 
    print("Smallest number:",min(numbers))
    print("Largest number:",max(numbers))
    
