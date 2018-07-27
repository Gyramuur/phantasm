import functions
import characters


class Entity:
    def __init__(self, name='Character', inventory=None, health=100, equip=None, c_room=None, target=None,
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
        self.target = target

    def spawn(self, room):
        room.characters.append(self)
        self.c_room = room

    def move(self, choice, available_rooms, widget):
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
                    description = "The door is locked."
                    functions.update_description(widget, description)
                    return

        else:
            print("You can't go that way.")

        description = self.c_room.room_desc()
        functions.update_description(widget, description)

    def take(self, widget, available_items):
        available_characters = ['']
        item = functions.get_target(widget.ids.text_input.text, available_items, available_characters)

        if item in self.c_room.items:
            self.c_room.items.remove(item)
            self.inventory.append(item)
            self.carrying += item.weight

            if self.carrying >= self.capacity:
                self.inventory.remove(item)
                self.c_room.items.append(item)
                self.carrying -= item.weight

        else:
            take_message = "You don't see that here.\n\n" + self.c_room.room_desc() + "\n"
            functions.update_description(widget, take_message)
            return

        if item in self.inventory:
            take_message = f"You take {item.name}.\n\n" + self.c_room.room_desc() + "\n"

        else:
            take_message = "That is too heavy!\n\n" + self.c_room.room_desc() + "\n"

        functions.update_description(widget, take_message)

    def drop(self, widget, available_items):
        available_characters = ['']
        if len(self.inventory) > 0:
            item = functions.get_target(widget.ids.text_input.text, available_items, available_characters)

            if item in self.inventory:
                self.inventory.remove(item)
                self.c_room.items.append(item)
                self.carrying -= item.weight
                drop_message = f"You drop {item.name}.\n\n{self.c_room.room_desc()}"
            else:
                drop_message = f"You are not carrying that.\n"

        else:
            drop_message = f"You don't have anything to drop!\n"

        functions.update_description(widget, drop_message)

    def say(self, widget):
        original_message = widget.ids.text_input.text
        message = f"{self.name}: {original_message[3:]}"
        functions.update_description(widget, message)  # This will have to change eventually, if you ever implement
        # multiplayer.


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

    def look(self, choice, available_items, available_characters, widget):
        if choice == 'look':
            functions.update_description(widget, self.c_room.room_desc())

        else:
            target = functions.get_target(choice, available_items, available_characters)
            if target in self.c_room.items or target in self.inventory:
                functions.update_description(widget, target.item_desc())
            elif target in self.c_room.characters:
                functions.update_description(widget, target.desc)
            else:
                functions.update_description(widget, "You don't see that here.")

    def player_choice(self, available_rooms, available_items, available_characters, choice, widget):

        if 'go' in choice:
            self.move(choice, available_rooms, widget)

        elif 'look' in choice:
            self.look(choice, available_items, available_characters, widget)

        elif 'take' in choice:
            self.take(widget, available_items)

        elif 'drop' in choice:
            self.drop(widget, available_items)

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

            functions.update_description(widget, stats)

        elif 'talk' in choice:
            # You need to make it so that this calls the in_conversation variable somehow so that it can modify
            # the behaviour of the readback function in game.py. Maybe make it so that entities can have an active
            # target, that way the code will be able to look at the target's conversation and access the in_conversation
            # variable. Try it out when you can.
            target = functions.get_target(choice, available_items, available_characters)
            # target.conversation.list_topics()
            if target in self.c_room.characters:
                self.target = target
                target.conversation.in_conversation = True
                target.conversation.conversation = target.conversation.initial_conversation

            else:
                functions.update_description(widget, "You don't see them here.")

        elif 'help' in choice:
            functions.update_description(widget, self.actions)

        elif 'say' in choice:
            self.say(widget)

        elif 'quit' in choice:
            exit(0)

        else:
            functions.update_description(widget, "You don't know how to do that.")

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
        description = f"{self.desc}\n" \
                      f"\nIt is worth: {self.value} gold." \
                      f"\nIt weighs {self.weight} pounds." \
                      f"\nIt does {self.damage} damage."

        return description


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