def get_season (month):
    season = month
    while True:
        if month == 1 or month == 2 or month == 12:
            print("You entered: " + str(month))
            print("The season is winter.")
            break

        if month== 3 or month == 4 or month == 5:
            print("You entered: " + str(month))
            print("The season is spring.")
            break

        if month== 6 or month == 7 or month == 8:
            print("You entered: " + str(month))
            print("The season is summer.")
            break

        if month== 9 or month == 10 or month == 11:
            print("You entered: " + str(month))
            print("The season is autumn.")
            break
        else:
            print("You entered: " + str(month))
            print("Please enter a number between 1 and 12.")

        return season

month = int(input("Enter the number of a month (1-12): "))

season = get_season(month)
