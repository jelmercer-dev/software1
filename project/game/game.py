import os

from . import Item, Player, Room
# from .player import Player
# from .room import Room
from .saves import load_game, save_game


# The project root is needed to read text files such as the intro and instructions.
PROJECT_DIRECTORY = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
        )
    )

# The tuple of Infinity Stones, player must collect.
INFINITY_STONES = (
    "Stone of Well-being",
    "Stone of Equality",
    "Stone of Nature",
    "Stone of Opportunity",
    "Stone of Cooperation",
)

# Function to display files like intrro.txt and instuctions.txt.
def show_startup_text(filename):

    try:
        file_path = os.path.join(PROJECT_DIRECTORY, filename)
        with open(file_path, "r") as file:
            text = file.read()
    except OSError:
        print(f"Could not read {filename}.")
        return

    print("\n" + text)

# Builds locations in the world and connects them.
def create_world(player_name):
    # Each room is a location with a name and optionally an item to collect.
    village = Room(
        "the Renewal Village",
        Item(INFINITY_STONES[0], 0.2),
    )
    riverlands = Room(
        "the Riverlands",
        Item(INFINITY_STONES[1], 0.2),
    )
    forest = Room(
        "the Living Forest",
        Item(INFINITY_STONES[2], 0.2),
    )
    highlands = Room(
        "the Knowledge Highlands",
        Item(INFINITY_STONES[3], 0.2),
    )
    commons = Room(
        "the Unity Commons",
        Item(INFINITY_STONES[4], 0.2),
    )

    # Connect rooms so the player can move around the world and choose different directions.
    village.connect("riverlands", riverlands)
    village.connect("highlands", highlands)
    riverlands.connect("highlands", highlands)
    riverlands.connect("village", village)
    forest.connect("riverlands", riverlands)
    forest.connect("highlands", highlands)
    forest.connect("unity commons", commons)
    highlands.connect("renewal village", village)
    highlands.connect("unity commons", commons)
    commons.connect("living forest", forest)
    commons.connect("knowledge highlands", highlands)

    # The player starts at the village, which is the first area of the map.
    return Player(player_name, village)

# Checks how many Infinity Stones the player has collected and returns the count.
def count_stones(player):
    collected = {item.name for item in player.items}
    return len(collected.intersection(INFINITY_STONES))

# Check whether the player has collected all Infinity Stones.
def has_all_stones(player):
    return count_stones(player) == len(INFINITY_STONES)

# Print the player's current inventory or a message if empty.
def show_inventory(player):
    if not player.items:
        print("\nYour inventory is empty.")
        return
    print("\nYour inventory:")
    for item in player.items:
        print(f"- {item}")

# Display the ending message when the player collected all stones.
def show_world_transformed():
    print(
        "\nThe five Infinity Stones unite! This world is transformed into "
        "a fairer, more sustainable place, working toward all 17 "
        "United Nations Sustainable Development Goals."
    )

# Diplays the menu of available actions based on player's current location and progress in the game.
def show_menu(player):

    exits = ", ".join(player.location.exits)
    print(f"\nLocation: {player.location.name}")
    print(f"Infinity Stones found: {count_stones(player)}/{len(INFINITY_STONES)}")
    print(f"\nAvailable destinations: {exits}\n")
    print("- w: Move to another room")
    print("- e: Collect the Infinity Stone in this room")
    print("- i: View your inventory")
    print("- r: Rest at the campfire")
    print("- v: Hear a fictional riddle")
    print("- lopeta: Quit the game")


# The main game loop, which handles player input and game state.
def run_game():

    show_startup_text("intro.txt")
    show_startup_text("instructions.txt") 

    name = input("\nEnter your name: ").strip() or "Tanos"  # Use "Tanos" as a default name if the player doesn't enter one.
    player = load_game(name) # Load a saved game if it exists.
    loaded_game = player is not None # Check if a saved game was loaded.
    # If the player is new, ask for their age and create a new world.
    while player is None:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Please enter your age as a number.")
            continue

        if age < 12:
            print(f"\n{name}, you are a minor and cannot play this game.")
            return

        player = create_world(name)
        print(f"\nWelcome, {player.name}! Starting a new game.")

    if loaded_game is True:
        print(f"\nWelcome back, {player.name}!") 

    # Show the starting room description and save the game.
    print(player.location.describe())
    save_game(player)

    if has_all_stones(player):
        show_world_transformed() 
        return

    # Main game loop
    while True:

        show_menu(player)
        command = input("\nEnter a command: ").lower().strip()
        # List of commands.
        if command in {"lopeta"}:
            save_game(player)
            print("\nGoodbye!")
            return
        if command in {"e"}:
            item = player.collect_item()
            if item:
                print(f"\nYou collected the {item.name}.")
                print(
                    f"Infinity Stones found: "
                    f"{count_stones(player)}/{len(INFINITY_STONES)}" # count the number of stones collected and display it
                )
            else:
                print("\nThere is no Infinity Stone to collect here.")
            save_game(player)
            if has_all_stones(player):
                show_world_transformed()
                return
            
        # Move a player to a new room.
        elif command == "w":
            direction = input("\nWhere would you like to go? ").lower().strip()
            if player.move(direction):
                print(player.location.describe())
                save_game(player)
            else:
                print("\nYou cannot go there from this room.")
        elif command in {"i"}:
            show_inventory(player)
        elif command in {"r"}:
            print("\nYou rest by the campfire.(game saved)")
            save_game(player)

        elif command in {"v"}:
            print("\nRiddle: What has keys but cannot open locks? A piano!")
        else:
            print("\nThat command is not on the menu.")