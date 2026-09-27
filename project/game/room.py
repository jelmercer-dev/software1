class Room:
    def __init__(self, name, item=None):
        self.name = name
        self.item = item
        self.exits = {}

    def connect(self, direction, room):
        self.exits[direction] = room

    def describe(self):
        description = f"You are in {self.name}."
        if self.item:
            description += f" You see a {self.item.name}."
        else:
            description += " There are no items here."
        return description