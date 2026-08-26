gender = input("Enter biological gender (male/female): ").strip().lower()

if gender == "male":
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))
    if hemoglobin < 134:
        print("Your hemoglobin is low.")
    if hemoglobin >= 134 and hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    if hemoglobin > 167:
        print("Your hemoglobin is high.")

elif gender == "female":
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))
    if hemoglobin < 117:
        print("Your hemoglobin is low.")
    if hemoglobin >= 117 and hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    if hemoglobin > 155:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")
