import classes
import items
import characters

start_room = classes.Room(
    desc="You are standing in a barren, stone-walled room. There is a door leading north.",
    exits={
        "north": "hallway",
    },
    items=[items.test_item, items.test_item2],
    characters=[characters.test_wolf]
)

hallway = classes.Room(
    desc="You are in a hallway. Before you is a doorway leading outside, and to the south is a door leading to an "
         "empty room.",
    exits={
        "south": "start_room",
        "outside": "sward"
    }
)

sward = classes.Room(
    desc="""You are standing in a meadow blanketed with softly-swaying grass. There is a house behind you and a small
cabin to the west.""",
    exits={
        "inside": "hallway",
        "west": "shop_front"
    },
    items=[items.heavy_test],
)

shop = classes.Room(
    desc="A lone candle flickers, illuminating the small wooden room. A door leads outside.",
    exits={
        "outside": "sward"
    },
    locked=True
)

shop_front = classes.Room(
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

