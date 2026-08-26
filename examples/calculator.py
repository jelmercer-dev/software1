option = input("Choose an option \n1. add \n2. subtract \n3. multiply \n4. divide \n5. exit \n \n") 

while option in ["1", "2", "3", "4", "5"]:
    
    option = input("Choose an option \n1. add \n2. subtract \n3. multiply \n4. divide \n5. exit \n \n")

    if option == "1":
        number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 + number2

if option == "2":
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 - number2

if option == "3":     
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 * number2

if option == "4":
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 / number2

if option == "5":
    print("Exiting the program.")

if option in ["1", "2", "3", "4"]:
    print(f"The result is: {result}")