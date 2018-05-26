import characters
import items
import rooms
from tkinter import *
from tkinter import ttk

characters.player.spawn(rooms.start_room)
characters.test_wolf.spawn(rooms.start_room)

root = Tk()
root.geometry("640x480")
root.configure(background="#000000")

game_text = StringVar()
player_choice = StringVar()

gui_style = ttk.Style()
gui_style.configure('My.TFrame', background='#000000', foreground='#FFFFFF')

content = ttk.Frame(root, style='My.TFrame')
entry = ttk.Entry(content, textvariable=player_choice)
text_field = Text(content, background="#000000", foreground="#FFFFFF")


content.grid(column=0, row=0, sticky=(N, W, E, S))
text_field.grid(column=0, row=1, sticky=(N,W, E, S))
entry.grid(column=0, row=2, sticky=(W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
text_field.columnconfigure(0, weight=1)
text_field.rowconfigure(0, weight=1)
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
    text_field.configure(state="disabled")
    root.mainloop()

    # while True:
        # characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters, game_text)


game()
# game()
