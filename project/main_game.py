def tutki(items):
	print("You discover a glowing shell on the shore.")
	item = input("What would you like to add to your inventory? ").strip()
	if item:
		items.append(item)
		print(f"{item} was added to your inventory.")
	else:
		print("You did not add an item.")


def nayta_esineet(items):
	if items:
		print("Your inventory:")
		for item in items:
			print(f"- {item}")
	else:
		print("Your inventory is empty.")


def lepaa():
	print("You rest by the campfire and regain your courage.")


def arvoitus():
	print("Riddle: What has keys but cannot open locks? A piano!")


name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))

if age < 12:
	print(f"{name}, you are a minor and cannot play this game.")
else:
	print(f"Welcome, {name}!")
	items = []

	while True:
		print("\nMain menu:")
		print("- tutki: Explore the mysterious island")
		print("- esineet: View your inventory")
		print("- lepaa: Rest at the campfire")
		print("- arvoitus: Hear a fictional riddle")
		print('- lopeta: Quit the game')

		command = input("Enter a command: ").lower().strip()

		if command == "lopeta":
			print("Game over. Goodbye!")
			break
		if command == "tutki":
			tutki(items)
		elif command == "esineet":
			nayta_esineet(items)
		elif command == "lepaa":
			lepaa()
		elif command == "arvoitus":
			arvoitus()
		else:
			print("That command is not on the menu.")

