import characters
import items
import rooms
from tkinter import *
from tkinter import ttk

characters.player.spawn(rooms.start_room)
characters.test_wolf.spawn(rooms.start_room)

root = Tk()
root.geometry("640x480")

game_text = StringVar()
player_choice = StringVar()

content = ttk.Frame(root)
entry = ttk.Entry(content, textvariable=player_choice)
entry_label = ttk.Label(content, text="> ")
text_field = Text(content)

content.grid(column=0, row=0, sticky=(N, W, E, S))
text_field.grid(column=1, row=0, sticky=(W, E))
entry.grid(column=1, row=1, sticky=(W, E, S))
entry_label.grid(column=0, row=1, sticky=(W, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
root.resizable(width=False, height=False)


def do_action(*args):
    choice = player_choice.get()
    characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters,
                                    choice, text_field)
    player_choice.set("")


button = ttk.Button(content, command=do_action)
root.bind('<Return>', do_action)
entry.focus()


def game():
    description = characters.player.c_room.room_desc()
    text_field.insert(END, description)
    root.mainloop()

    # while True:
        # characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters, game_text)


game()
# game()
