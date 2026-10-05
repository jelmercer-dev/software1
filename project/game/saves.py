import json
import os

from .item import Item



SAVE_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "save.json",
)


def _get_rooms(starting_room):
    rooms = {}
    rooms_to_visit = [starting_room]
    while rooms_to_visit:
        room = rooms_to_visit.pop()
        if room.name in rooms:
            continue
        rooms[room.name] = room
        rooms_to_visit.extend(room.exits.values())
    return rooms


def save_game(player):
    rooms = _get_rooms(player.location)
    state = {
        "player_name": player.name,
        "location": player.location.name,
        "inventory": [
            {"name": item.name, "weight": item.weight} for item in player.items
        ],
        "room_items": {
            room.name: (
                {"name": room.item.name, "weight": room.item.weight}
                if room.item else None
            )
            for room in rooms.values()
        },
    }

    saved_games = {}
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as file:
                saved_games = json.load(file)
        except (OSError, ValueError):
            print("The save file could not be read. Your progress was not saved.")
            return
        if not isinstance(saved_games, dict):
            print("The save file has an invalid format. Your progress was not saved.")
            return

    saved_games[player.name.casefold()] = state
    try:
        with open(SAVE_FILE, "w") as file:
            json.dump(saved_games, file, indent=2)
    except OSError:
        print("The game could not be saved.")


def load_game(player_name):
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r") as file:
            saved_games = json.load(file)
        if not isinstance(saved_games, dict):
            raise TypeError("Invalid save file format")
        state = saved_games.get(player_name.casefold())
        if state is None:
            return None
        if state["player_name"].casefold() != player_name.casefold():
            return None

        from .game import create_world

        player = create_world(state["player_name"])
        rooms = _get_rooms(player.location)
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