# Island Adventure

Denys Khliustin

## Project structure

The game is split into a small package so that each class has one clear responsibility:


project/
├── main_game.py       # Starts the game
├── readme.md          # Project documentation
└── game/
	├── __init__.py    # Exposes Item, Player, and Room
	├── game.py        # Creates the world and runs the menu
	├── item.py        # Item class
	├── player.py      # Player class and player actions
	└── room.py        # Room class and room connections


`Player` stores the player's name, inventory, and current room. `Room` stores its name, exits, and an optional item. `Item` stores an item's name and weight. At startup, the game creates one player, three rooms, and three items. The menu lets the player move between connected rooms, collect items, view the inventory, rest, hear a riddle, or quit.

