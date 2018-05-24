import characters
import items
import rooms
from tkinter import *
from tkinter import ttk

characters.player.spawn(rooms.start_room)
characters.test_wolf.spawn(rooms.start_room)

root = Tk()

game_text = StringVar()
player_choice = StringVar()

content = ttk.Frame(root)
entry = ttk.Entry(content, textvariable=player_choice)
text_field = ttk.Label(content, textvariable=game_text)

content.grid(column=0, row=0, sticky=(N, W, E, S))
text_field.grid(column=0, row=0, sticky=(W, E))
entry.grid(column=0, row=1, sticky=(W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.rowconfigure(1, weight=1)


def do_action(*args):
    choice = player_choice.get()
    characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters,
                                    choice, game_text)
    player_choice.set("")


button = ttk.Button(content, command=do_action)
button.grid(column=1, row=1, sticky=(E, S))
root.bind('<Return>', do_action)
entry.focus()


def game():
    description = characters.player.c_room.room_desc()
    game_text.set(description)
    root.mainloop()

    # while True:
        # characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters, game_text)


game()
# game()
