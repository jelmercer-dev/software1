
numbers = []

number = input("Enter: ")

while number != "":
    numbers.append(float(number))
    number = input("Enter the next name or quit by pressing Enter: ")

if numbers: 
    print("Largest: ", max(numbers))
    print("Smallest: ", min(numbers))



# for n in numbers:
#     print("Hello!", max(n))
#     print("Hello!", min(n))