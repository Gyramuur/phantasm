import characters
import items
import rooms
from tkinter import *
from tkinter import ttk

characters.player.spawn(rooms.start_room)
characters.test_wolf.spawn(rooms.start_room)


def game():

    characters.player.c_room.room_desc()

    while True:
        characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters)


game()
