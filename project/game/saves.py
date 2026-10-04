import hashlib
import json
from pathlib import Path

from .item import Item
from .player import Player


SAVES_DIRECTORY = Path(__file__).resolve().parent.parent / "saves"


def _save_path(player_name):
    player_key = hashlib.sha256(player_name.casefold().encode("utf-8")).hexdigest()
    return SAVES_DIRECTORY / f"{player_key}.json"


def _rooms_from(starting_room):
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
    rooms = _rooms_from(player.location)
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
    SAVES_DIRECTORY.mkdir(parents=True, exist_ok=True)
    _save_path(player.name).write_text(
        json.dumps(state, indent=2), encoding="utf-8"
    )


def load_game(player_name):
    save_path = _save_path(player_name)
    if not save_path.exists():
        return None

    try:
        state = json.loads(save_path.read_text(encoding="utf-8"))
        if state["player_name"].casefold() != player_name.casefold():
            return None

        from .game import create_world

        player = create_world(state["player_name"])
        rooms = _rooms_from(player.location)
        player.location = rooms[state["location"]]
        player.items = [Item(item["name"], item["weight"]) for item in state["inventory"]]
        for room_name, item in state["room_items"].items():
            if room_name in rooms:
                rooms[room_name].item = (
                    Item(item["name"], item["weight"]) if item else None
                )
        return player
    except (OSError, ValueError, KeyError, TypeError):
        print("The saved game could not be loaded. Starting a new game instead.")
        return None