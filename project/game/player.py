class Player:
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, direction):
        destination = self.location.exits.get(direction)
        if destination is None:
            return False
        self.location = destination
        return True

    def collect_item(self):
        if self.location.item is None:
            return None
        item = self.location.item
        self.items.append(item)
        self.location.item = None
        return item