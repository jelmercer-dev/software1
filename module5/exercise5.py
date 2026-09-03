attempts = 0

username = "python"
password = "rules"

username = input("Enter username: ")
password = input("Enter password: ")

while username != "python" or password != "rules":
    print ("Incorrect username or password. Please try again.")

    username = input("Enter username: ")
    password = input("Enter password: ")

    attempts += 1
    if attempts >= 4:
        print("Access denied")
        break

if username == "python" and password == "rules":
    print("Welcome")