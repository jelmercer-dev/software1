option = input("Choose an option: \n1. add \n2. subtract \n3. multiply \n4. divide \n0. exit \n \n")

while option != "0":

        if option == "1":  
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            result = number1 + number2

        elif option == "2":
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            result = number1 - number2

        elif option == "3":
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            result = number1 * number2

        elif option == "4":
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            result = number1 / number2

        else:
            print("Invalid option. Please choose a valid option.")
            option = input("Choose an option: \n1. add \n2. subtract \n3. multiply \n4. divide \n0. exit \n \n")
        print(f"The result is: {result}")

        
        

if option == "0":
    print("Exiting the program.")


