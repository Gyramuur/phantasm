import characters
import items
import rooms
import functions
import conversations
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView


characters.player.spawn(rooms.start_room)
# characters.test_wolf.spawn(rooms.start_room)
items.stick.spawn(rooms.start_room, items)
items.chest.spawn(rooms.hallway, items)

Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
        font_name: "Legendaria.ttf"
        color: [.494, .152, .074, 1]
        padding: (10, 10)
        font_size: 26
''')


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class MainWidget(Widget):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("Main Widget.")
        self.ids.game_label.game_text = characters.player.c_room.room_desc()
        self.ids.text_input.focus = True

    def readback(self):

        if characters.player.target is not None:
            print("Has target.")
            if characters.player.target.is_living:
                if characters.player.target.conversation.in_conversation:
                    print("Top level converse.")
                    characters.player.target.conversation.converse(self, self.ids.text_input.text)
            else:
                print("Lost target.")
                characters.player.player_choice(rooms.available_rooms, items.available_items,
                                                characters.available_characters, self.ids.text_input.text, self)
        else:
            print("Normal choice.")
            characters.player.player_choice(rooms.available_rooms, items.available_items,
                                            characters.available_characters, self.ids.text_input.text, self)


        self.ids.text_input.text = ""
        self.ids.game_text = ""
        self.ids.text_input.focus = True

    def do_readback(self):
        Clock.schedule_once(lambda dt: self.readback())


class PhantasmApp(App):
    def build(self):
        return MainWidget()


'''
def game():
    description = characters.player.c_room.room_desc()
    text_field.insert(END, description)
    text_field.configure(state="disabled")
    root.mainloop()

    # while True:
        # characters.player.player_choice(rooms.available_rooms, items.available_items, characters.available_characters, game_text)'''

# game()


if __name__ == "__main__":
    PhantasmApp().run()
