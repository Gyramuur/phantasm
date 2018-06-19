import characters
import items
import rooms
from tkinter import *
from tkinter import ttk


characters.player.spawn(rooms.start_room)
characters.test_wolf.spawn(rooms.start_room)

root = Tk()
root.configure(background="#e2c69d")
root.title("Phantasm")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

game_text = StringVar()
player_choice = StringVar()

gui_style = ttk.Style()
gui_style.configure('My.TFrame', background='#e2c69d', foreground='#FFFFFF')

content = ttk.Frame(root, style='My.TFrame', padding='5 5 5 5')
content2 = ttk.Frame(root, style='My.TFrame', padding='5 5 5 5')

game_font = ("Legendaria", 24, 'bold')

entry = Entry(content2, textvariable=player_choice, background='#e2c69d', foreground='#7e2713', borderwidth=0,
              highlightthickness=0, insertbackground='#7e2713', font=game_font)
entry_label = Label(content2, text="> ", background='#e2c69d', foreground='#7e2713', font=game_font)
text_field = Text(content, background='#e2c69d', foreground="#7e2713", borderwidth=0, font=game_font,
                  wrap=WORD)


'''
content.grid(column=0, row=0, sticky=(N, W, E, S))
entry_label.grid(row=2, sticky=W)
entry.grid(column=1, row=2, sticky=W, columnspan=2)
text_field.grid(columnspan=2, row=1, sticky=(N, W, E, S))'''

content.grid(sticky=(N, W), column=0, row=0)
content2.grid(sticky=(S, W), column=0, row=0)
text_field.grid(column=0, sticky=(N, W))
entry_label.grid(column=0, row=0, sticky=(S, W))
entry.grid(column=1, row=0, sticky=(S, W))

content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)
content2.columnconfigure(0, weight=1)
content2.rowconfigure(1, weight=1)
text_field.columnconfigure(0, weight=1)
text_field.rowconfigure(0, weight=1)

if root.winfo_width() > screen_width and root.winfo_height() > screen_height:
    root.geometry(f"{screen_width}x{screen_height}")

root.resizable(width=False, height=False)


def do_action(*args):
    choice = player_choice.get()
    characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters,
                                    choice, text_field)
    player_choice.set("")


def return_focus(*args):
    entry.focus()


# button = ttk.Button(content, command=do_action)
root.bind('<Return>', do_action)
root.bind('<Button-1>', return_focus)
return_focus()


def game():
    description = characters.player.c_room.room_desc()
    text_field.insert(END, description)
    text_field.configure(state="disabled")
    root.mainloop()

    # while True:
        # characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters, game_text)


game()
# game()
