def get_season(month):
    
    winter = (1, 2, 12)
    spring = (3, 4, 5)
    summer = (6, 7, 8)
    autumn = (9, 10, 11)

    if month in winter:
        season = "winter"

    elif month in spring:
        season = "spring"

    elif month in summer:
        season = "summer"

    elif month in autumn:
        season = "autumn"

    else:
        print("You entered: "+ str(month))
        print("Please enter a number between 1 and 12.")
        return

    print("You entered:", month)
    print("The season is", season + ".")


month = int(input("Enter the number of a month (1-12): "))
get_season(month)