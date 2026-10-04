from .item import Item
from .player import Player
from .room import Room
from .saves import load_game, save_game

from pathlib import Path


PROJECT_DIRECTORY = Path(__file__).resolve().parent.parent


def show_startup_text(filename):
    try:
        text = (PROJECT_DIRECTORY / filename).read_text(encoding="utf-8")
    except OSError:
        print(f"Could not read {filename}.")
        return
    print(text)


def create_world(player_name):
    beach = Room("the beach", Item("glowing shell", 0.2))
    forest = Room("the forest", Item("compass", 0.4))
    cave = Room("the cave", Item("lantern", 1.5))

    beach.connect("forest", forest)
    forest.connect("beach", beach)
    forest.connect("cave", cave)
    cave.connect("forest", forest)

    return Player(player_name, beach)


def show_inventory(player):
    if not player.items:
        print("Your inventory is empty.")
        return
    print("Your inventory:")
    for item in player.items:
        print(f"- {item}")


def show_menu(player):
    exits = ", ".join(player.location.exits)
    print(f"\nLocation: {player.location.name}")
    print(f"\nAvailable destinations: {exits}\n")
    print("- w: Move to another room")
    print("- e: Collect the item in this room")
    print("- i: View your inventory")
    print("- r: Rest at the campfire")
    print("- v: Hear a fictional riddle")
    print("- lopeta: Quit the game")


def run_game():
    show_startup_text("intro.txt")
    show_startup_text("instructions.txt")
    name = input("Enter your name: ").strip() or "Adventurer"
    player = load_game(name)
    while player is None:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Please enter your age as a number.")
            continue

        if age < 12:
            print(f"{name}, you are a minor and cannot play this game.")
            continue

        player = create_world(name)
        print(f"Welcome, {player.name}! Starting a new game.")
    else:
        print(f"Welcome back, {player.name}! Your saved game has been restored.")

    print(player.location.describe())
    save_game(player)

    while True:
        show_menu(player)
        command = input("\nEnter a command: ").lower().strip()

        if command in {"lopeta"}:
            save_game(player)
            print("Game over. Goodbye!")
            return
        if command in {"e"}:
            item = player.collect_item()
            print(f"\nYou collected the {item.name}.") if item else print("There is no item to collect here.")
            save_game(player)
        elif command == "w":
            direction = input("Where would you like to go? ").lower().strip()
            if player.move(direction):
                print(player.location.describe())
                save_game(player)
            else:
                print("You cannot go there from this room.")
        elif command in {"i"}:
            show_inventory(player)
        elif command in {"r"}:
            print("You rest by the campfire and regain your courage.")
        elif command in {"v"}:
            print("Riddle: What has keys but cannot open locks? A piano!")
        else:
            print("That command is not on the menu.")