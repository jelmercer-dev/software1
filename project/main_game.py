name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
	print(f"{name}, you are a minor and cannot play this game.")
else:
	print(f"Welcome, {name}!")

	while True:
		print("\nMain menu:")
		print("- tutki: Explore the mysterious island")
		print("- lepaa: Rest at the campfire")
		print("- arvoitus: Hear a fictional riddle")
		print('- lopeta: Quit the game')

		command = input("Enter a command: ").lower()

		if command == "lopeta":
			print("Game over. Goodbye!")
			break
		if command == "tutki":
			print("You discover a glowing shell on the shore.")
		elif command == "lepaa":
			print("You rest by the campfire and regain your courage.")
		elif command == "arvoitus":
			print("Riddle: What has keys but cannot open locks? A piano!")
		else:
			print("That command is not on the menu.")

