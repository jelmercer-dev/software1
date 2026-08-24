talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kilograms = total_grams / 1000
remaining_grams = total_grams % 1000

print(f"The weight in modern units:\n{int(kilograms):d} kilograms and {remaining_grams:.2f} grams.")
