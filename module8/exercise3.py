airports = {}

while True:
	print("\nAirport Data Management")
	print("1. Enter a new airport")
	print("2. Fetch airport information")
	print("3. Quit")
	print("Please choose an option (1-3): ")

	choice = input()
	if choice == "1":
		icao = input("Enter the ICAO code: ").strip()
		name = input("Enter the airport name: ").strip()
		airports[icao] = name
		print("Airport", name, "with ICAO code", icao, "has been added.")

	elif choice == "2":
		icao = input("Enter the ICAO code: ").strip()
		if icao in airports:
			print(f"The airport with ICAO code {icao} is {airports[icao]}.")
		else:
			print(f"No airport found with ICAO code {icao}.")

	elif choice == "3":
		print("Thank you for using the Airport Data Management system. Goodbye!")
		break
