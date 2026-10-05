import os

from .item import Item
from .player import Player
from .room import Room
from .saves import load_game, save_game


PROJECT_DIRECTORY = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
        )
    )

INFINITY_STONES = (
    "Stone of Well-being",
    "Stone of Equality",
    "Stone of Nature",
    "Stone of Opportunity",
    "Stone of Cooperation",
)


def show_startup_text(filename):
    try:
        file_path = os.path.join(PROJECT_DIRECTORY, filename)
        with open(file_path, "r") as file:
            text = file.read()
    except OSError:
        print(f"Could not read {filename}.")
        return
    print("\n" + text)


def create_world(player_name):
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

    village.connect("riverlands", riverlands)
    village.connect("knowledge highlands", highlands)
    riverlands.connect("renewal village", village)
    riverlands.connect("living forest", forest)
    forest.connect("riverlands", riverlands)
    forest.connect("unity commons", commons)
    highlands.connect("renewal village", village)
    highlands.connect("unity commons", commons)
    commons.connect("living forest", forest)
    commons.connect("knowledge highlands", highlands)

    return Player(player_name, village)


def count_stones(player):
    collected = {item.name for item in player.items}
    return len(collected.intersection(INFINITY_STONES))


def has_all_stones(player):
    return count_stones(player) == len(INFINITY_STONES)


def show_world_transformed():
    print(
        "\nThe five Infinity Stones unite! This world is transformed into "
        "a fairer, more sustainable place, working toward all 17 "
        "United Nations Sustainable Development Goals."
    )


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
    print(f"Infinity Stones found: {count_stones(player)}/{len(INFINITY_STONES)}")
    print(f"\nAvailable destinations: {exits}\n")
    print("- w: Move to another room")
    print("- e: Collect the Infinity Stone in this room")
    print("- i: View your inventory")
    print("- r: Rest at the campfire")
    print("- v: Hear a fictional riddle")
    print("- lopeta: Quit the game")


def run_game():
    show_startup_text("intro.txt")
    show_startup_text("instructions.txt")
    name = input("\nEnter your name: ").strip() or "Adventurer"
    player = load_game(name)
    while player is None:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Please enter your age as a number.")
            continue

        if age < 12:
            print(f"{name}, you are a minor and cannot play this game.")
            return

        player = create_world(name)
        print(f"Welcome, {player.name}! Starting a new game.")
    else:
        print(f"Welcome back, {player.name}! Your saved game has been restored.")

    print(player.location.describe())
    save_game(player)
    if has_all_stones(player):
        show_world_transformed()
        return

    while True:
        show_menu(player)
        command = input("\nEnter a command: ").lower().strip()

        if command in {"lopeta"}:
            save_game(player)
            print("Game over. Goodbye!")
            return
        if command in {"e"}:
            item = player.collect_item()
            if item:
                print(f"\nYou collected the {item.name}.")
                print(
                    f"Infinity Stones found: "
                    f"{count_stones(player)}/{len(INFINITY_STONES)}"
                )
            else:
                print("There is no Infinity Stone to collect here.")
            save_game(player)
            if has_all_stones(player):
                show_world_transformed()
                return
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
            print("You rest by the campfire and regain your courage.(game saved)")
            save_game(player)
        elif command in {"v"}:
            print("Riddle: What has keys but cannot open locks? A piano!")
        else:
            print("That command is not on the menu.")