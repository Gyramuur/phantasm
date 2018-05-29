import functions
import characters

class Entity:
    def __init__(self, name='Character', inventory=None, health=100, equip=None, c_room=None,
                 desc='You see nothing remarkable.', capacity=20, carrying=0, conversation=None, disposition=50):
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
        self.conversation = conversation
        self.disposition = disposition

    def spawn(self, room):
        room.characters.append(self)
        self.c_room = room

    def move(self, choice, available_rooms, game_text):
        direction = functions.get_direction(choice)

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

        description = self.c_room.room_desc()
        functions.update_description(description, choice, game_text)

    def take(self, choice, available_items, game_text):
        available_characters = ['']
        item = functions.get_target(choice, available_items, available_characters)

        if item in self.c_room.items:
            self.c_room.items.remove(item)
            self.inventory.append(item)
            self.carrying += item.weight

            if self.carrying >= self.capacity:
                self.inventory.remove(item)
                self.c_room.items.append(item)
                self.carrying -= item.weight

        else:
            take_message="You don't see that here.\n"
            functions.update_description(take_message, choice, game_text)
            return

        if item in self.inventory:
            take_message = f"You take {item.name}.\n"

        else:
            take_message = "That is too heavy!\n"

        functions.update_description(take_message, choice, game_text)

    def drop(self, choice, available_items, game_text):
        available_characters = ['']
        if len(self.inventory) > 0:
            item = functions.get_target(choice, available_items, available_characters)

            if item in self.inventory:
                self.inventory.remove(item)
                self.c_room.items.append(item)
                self.carrying -= item.weight
                drop_message = f"You drop {item.name}.\n"
            else:
                drop_message = f"You are not carrying that.\n"

        else:
            drop_message = "You don't have anything to drop!\n"

        functions.update_description(drop_message, choice, game_text)


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

    def look(self, choice, available_items, available_characters, game_text):
        if choice == 'look':
            description = self.c_room.room_desc()
            functions.update_description(description, choice, game_text)

        else:
            target = functions.get_target(choice, available_items, available_characters)
            if target in self.c_room.items or target in self.inventory:
                target.item_desc()
            elif target in self.c_room.characters:
                print(target.desc)
            else:
                print("You don't see that here.")

    def player_choice(self, available_rooms, available_items, available_characters, choice, game_text):

        if 'go' in choice:
            self.move(choice, available_rooms, game_text)

        elif 'look' in choice:
            self.look(choice, available_items, available_characters, game_text)

        elif 'take' in choice:
            self.take(choice, available_items, game_text)

        elif 'drop' in choice:
            self.drop(choice, available_items, game_text)

        elif 'check' in choice:
            if len(self.inventory) > 0:
                inventory = "\nYou are carrying:\n"

                for item in self.inventory:
                    inventory = inventory + item.name + "\n"

            else:
                inventory = ""

            stats = f"Name: {self.name}" + "\n" \
                    f"Health: {self.health}" + "\n" \
                    f"{inventory}" + "\n" \
                    f"Encumbrance: {self.carrying}/{self.capacity}" + "\n"

            functions.update_description(stats, choice, game_text)

            '''
            print("Name: " + self.name)
            print(f"Health: {self.health}\n")
            if len(self.inventory) > 0:
                print("You are carrying:")
                for item in self.inventory:
                    print(item.name)
            print(f"Encumbrance: {self.carrying}/{self.capacity}")
            '''

        elif 'talk' in choice:
            target = functions.get_target(choice, available_items, available_characters)
            # target.conversation.list_topics()
            if target in self.c_room.characters:
                target.conversation.converse()
            else:
                print("You don't see them here.")

        elif 'help' in choice:
            functions.update_description(self.actions, choice, game_text)

        elif 'quit' in choice:
            exit(0)

        else:
            print("You don't know how to do that.")

        print()


class Item:
    def __init__(self, name='item', desc='', value=1, damage=1, unlocks='', edible=False, container=False,
                 capacity=0, weight=1):
        self.name = name
        self.desc = desc
        self.value = value
        self.damage = damage
        self.unlocks = unlocks
        self.edible = edible
        self.container = container
        self.capacity = capacity
        self.weight = weight

    def item_desc(self):
        print(self.desc)
        print(f"It is worth: {self.value} gold.")
        print(f"It weighs {self.weight} pounds.")
        print(f"It does {self.damage} damage.")


class Room:
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

        # Rewrite this to update the game_text variable instead.

        room_description = []
        room_description.append(self.desc)

        description_string = ""

        for item in self.items:
            room_description.append(f"A {item.name} is here.")

        for character in self.characters:
            if character.name != characters.player.name:
                room_description.append(f"{character.name.title()} is standing here.")

        for item in room_description:
            description_string += (item + "\n")

        return description_string


        '''
        print(self.desc)

        for item in self.items:
            print("There is a " + item.name + " here.")

        for character in self.characters:
            if character.name != "Scintilla":
                print(character.name + " is standing here.")
                '''

    def spawn(self, character):
        self.characters.append(character)