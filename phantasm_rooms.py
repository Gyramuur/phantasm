import phantasm_items as phitems
import phantasm_characters as phcharacters


class Room():
    def __init__(self, desc="An empty, unused room.", items=None, characters=None, exterior=False, locked=False,
                 exits=None):
        if exits is None:
            exits = {}
        if characters is None:
            characters = []
        if items is None:
            items = []
        self.desc = desc
        self.items = items
        self.characters = characters
        self.exterior = exterior
        self.locked = locked
        self.exits = exits

    def room_desc(self):
        print(self.desc)

        for item in self.items:
            print("There is a " + item.name + " here.")

        for character in self.characters:
            if character.name != "Scintilla":
                print(character.name + " is standing here.")

    def spawn(self, character):
        self.characters.append(character)
