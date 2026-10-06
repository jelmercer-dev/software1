import json
import os
from .item import Item


# The path to the save file.
# Getting the absolute path to the project directory,
# going two folders up and combining it into a single path.
SAVE_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "save.json",
)

# A function to get all exits from a starting room.
def get_rooms (starting_room):
    rooms = {}
    rooms_to_visit = [starting_room] # list of rooms to visit 
    while rooms_to_visit:
        room = rooms_to_visit.pop() # takes the last room from the list

        if room.name in rooms:
            continue
    
        rooms[room.name] = room # adding the room to the dictionary
        rooms_to_visit.extend(room.exits.values()) # extending the list of rooms to visit with the exits of the current room
    return rooms

# saving the state of the game to a JSON file.
def save_game(player): # creates a save with the specified player's name
    rooms = get_rooms(player.location) # get all available rooms from the player's current room
    # info to save in JSON file
    state = {
        "player_name": player.name,
        "location": player.location.name,
        "inventory": [
            {"name": item.name, "weight": item.weight} for item in player.items  # dictionary for every item in the player's inventory
        ],
        "room_items": {
            room.name: (
                {"name": room.item.name, "weight": room.item.weight}  # dictionarry for every item in the room if it exists
                if room.item else None
            )
            for room in rooms.values() # repeats for every room in the dictionary of rooms
        },
    }

    saved_games = {}
    if os.path.exists(SAVE_FILE):  # check if the save file exists
        try:
            with open(SAVE_FILE, "r") as file:
                saved_games = json.load(file)
        except(OSError):
            print("Can't open the file.")
            return


    saved_games[player.name.casefold()] = state  # updates the save of a player 
    try:
        with open(SAVE_FILE, "w") as file:
            json.dump(saved_games, file, indent=2)
    except OSError:
        print("The game could not be saved.")

# loading the sstate of the game 
def load_game(player_name):  # loads a save with the specified player's name
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r") as file:
            saved_games = json.load(file)
        state = saved_games.get(player_name.casefold())
        if state is None:
            return None
        if state["player_name"].casefold() != player_name.casefold():
            return None

        from .game import create_world

        player = create_world(state["player_name"])
        rooms = get_rooms(player.location)
        player.location = rooms[state["location"]]
        player.items = [
            Item(item["name"], item["weight"]) for item in state["inventory"]
        ]
        for room_name, item in state["room_items"].items():
            if room_name in rooms:
                rooms[room_name].item = (
                    Item(item["name"], item["weight"]) if item else None
                )
        return player
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        print("The saved game could not be loaded. Starting a new game instead.")
        return None