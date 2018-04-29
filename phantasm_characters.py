from sys import exit
import phantasm_functions as phfuncs


class Entity():
    def __init__(self, name='Character', inventory=None, health=100, equip=None, c_room=None,
                 desc='You see nothing remarkable.', capacity=20, carrying=0):
        if equip is None:
            equip = []
        if inventory is None:
            inventory = []
        self.name = name
        self.inventory = inventory
        self.health = health
        self.equip = equip
        self.c_room = c_room
        self.desc = desc
        self.capacity = capacity
        self.carrying = carrying

    def spawn(self, room):
        room.characters.append(self)
        self.c_room = room

    def move(self, choice, available_rooms):
        direction = phfuncs.get_direction(choice)

        if direction in self.c_room.exits:
            direction = self.c_room.exits[direction]
            target_room = available_rooms[direction]
            if not target_room.locked:
                if self in self.c_room.characters:
                    self.c_room.characters.remove(self)
                self.c_room = available_rooms[direction]
                self.c_room.characters.append(self)

            else:
                if self.name == "Scintilla":
                    print("The door is locked.")

        else:
            print("You can't go that way.")

        self.c_room.room_desc()

    def take(self, choice, available_items):
        available_characters = ['']
        item = phfuncs.get_target(choice, available_items, available_characters)

        if item in self.c_room.items:
            self.c_room.items.remove(item)
            self.inventory.append(item)
            self.carrying += item.weight

            if self.carrying >= self.capacity:
                print("That is too heavy!")
                self.inventory.remove(item)
                self.c_room.items.append(item)
                self.carrying -= item.weight
                return

        else:
            print("You don't see that here.")
            return

        print(f"You take {item.name}.")

    def drop(self, choice, available_items):
        available_characters = ['']
        if len(self.inventory) > 0:
            item = phfuncs.get_target(choice, available_items, available_characters)

            if item in self.inventory:
                self.inventory.remove(item)
                self.c_room.items.append(item)
                self.carrying -= item.weight
                print(f"You drop {item.name}")
            else:
                print("You can't lose what you don't have.")

        else:
            print("You don't have anything to drop!")


class Player(Entity):
    actions = '''
You can:

go <direction> - Move in a specified direction.	

look - Shows description of current room and its contents.

look <at something> - Shows description of specified object.

take <item> - Takes the specified item if present.

drop <item> - Drops specified item if in inventory.

check - Displays name, health, and contents of inventory.

quit - Quits the game.'''

    def look(self, choice, available_items, available_characters):
        if choice == 'look':
            self.c_room.room_desc()

        else:
            target = phfuncs.get_target(choice, available_items, available_characters)
            if target in self.c_room.items or target in self.inventory:
                target.item_desc()
            elif target in self.c_room.characters:
                print(target.desc)
            else:
                print("You don't see that here.")

    def player_choice(self, available_rooms, available_items, available_characters):
        choice = input('> ')

        print()

        if 'go' in choice:
            self.move(choice, available_rooms)

        elif 'look' in choice:
            self.look(choice, available_items, available_characters)

        elif 'take' in choice:
            self.take(choice, available_items)

        elif 'drop' in choice:
            self.drop(choice, available_items)

        elif 'check' in choice:
            print("Name: " + self.name)
            print(f"Health: {self.health}\n")
            if len(self.inventory) > 0:
                print("You are carrying:")
                for item in self.inventory:
                    print(item.name)
            print(f"Encumbrance: {self.carrying}/{self.capacity}")

        elif 'help' in choice:
            print(self.actions)

        elif 'quit' in choice:
            exit(0)

        else:
            print("You don't know how to do that.")

        print()




