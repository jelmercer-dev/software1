def calculate_unit_price(diameter, price):
    import math
    result = price / (math.pi * (diameter / 2 / 100) ** 2)
    return result

diameter = float(input("Enter the diameter of the first pizza (cm): "))
price = float(input("Enter the price of the first pizza (euros): "))
first_pizza = calculate_unit_price(diameter, price)


diameter = float(input("Enter the diameter of the second pizza (cm): "))
price = float(input("Enter the price of the second pizza (euros): "))
second_pizza = calculate_unit_price(diameter, price)

print(f"Unit price of the first pizza: {first_pizza:.2f} euros/m²")
print(f"Unit price of the second pizza: {second_pizza:.2f} euros/m²")

if first_pizza < second_pizza:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")