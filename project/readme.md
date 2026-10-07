# The Five Stones of a Better World

Denys Khliustin

## Project structure

The game is split into a small package so that each class has one clear responsibility:


project/

├── main_game.py       # Starts the game

├── intro.txt          # Introductory text shown at startup

├── instructions.txt   # Player instructions shown at startup

├── save.json          # Player saves (created automatically)

├── readme.md          # Project documentation

└── game/

	├── __init__.py    # Exposes Item, Player, and Room
	
	├── game.py        # Creates the world and runs the menu
	
	├── item.py        # Item class
	
	├── player.py      # Player class and player actions
	
	├── room.py        # Room class and room connections
	
	└── saves.py       # Saves and restores game state


`Player` stores the player's name, inventory, and current room. `Room` stores its name, exits, and an optional item. `Item` stores an item's name and weight. At startup, the game reads `intro.txt` and `instructions.txt`, then creates one player and a connected world of five locations, each containing one unique Infinity Stone, unless a save exists for the entered name. Collect all five stones to complete the adventure and transform the world toward all 17 United Nations Sustainable Development Goals. Progress is automatically saved as JSON text in `save.json`, including the player's location, inventory, and remaining room items. Enter the same name at startup to continue that player's game.
