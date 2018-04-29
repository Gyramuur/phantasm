import phantasm_characters as phcharacters
import phantasm_rooms as phrooms
import phantasm_items as phitems
# Needs save-game stuff here.

# Characters
player = phcharacters.Player(name='Scintilla')

test_wolf = phcharacters.Entity(name='Wolf',
                                desc='A large gray wolf. He looks happy.')

available_characters = {
    'self': player,
    'wolf': test_wolf
}

# Items
test_item = phitems.Item(
    name='mysterious orb',
    desc='A strange orb that is slowly pulsing, alternating between hues of lavender and cerulean.',
    value=1000
)

test_item2 = phitems.Item(
    name='cube',
    desc="It's a cube! Or maybe it's a tesseract?",
    value=1000
)

heavy_test = phitems.Item(
    name='statue of the night goddess',
    desc='A tall statue of the night goddess, carved from white marble.',
    value=10000,
    weight=10000
)

available_items = {
    'orb': test_item,
    'cube': test_item2,
    'statue': heavy_test
}

# Rooms
start_room = phrooms.Room(
    desc="You are standing in a barren, stone-walled room. There is a door leading north.",
    exits={
        "north": "hallway",
    },
    items=[test_item, test_item2]
)

hallway = phrooms.Room(
    desc="You are in a hallway. Before you is a doorway leading outside, and to the south is a door leading\n" +
    "to an empty room",
    exits={
        "south": "start_room",
        "outside": "sward"
    }
)

sward = phrooms.Room(
    desc="""You are standing in a meadow blanketed with softly-swaying grass. There is a house behind you and a small
cabin to the west.""",
    exits={
        "inside": "hallway",
        "west": "shop_front"
    },
    items=[heavy_test],
)

shop = phrooms.Room(
    desc="A lone candle flickers, illuminating the small wooden room. A door leads outside.",
    exits={
        "outside": "sward"
    },
    locked=True
)

shop_front = phrooms.Room(
    desc="""You stand before an old, dilapidated house. A sign hangs above the door, reading 'Jabari's Wares'.
There is a door leading inside and a meadow to the east.""",
    exits={
        "inside": "shop",
        "east": "sward"
    }
)

available_rooms = {
    "hallway": hallway,
    "start_room": start_room,
    "sward": sward,
    "shop": shop,
    "shop_front": shop_front
}

player.spawn(start_room)
test_wolf.spawn(sward)


def game():

    player.c_room.room_desc()

    while True:
        player.player_choice(available_rooms, available_items, available_characters)


game()
