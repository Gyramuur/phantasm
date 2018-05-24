import classes
import conversations

player = classes.Player(name='Scintilla')

test_wolf = classes.Entity(name='Wolf',
                                desc='A large gray wolf. He looks happy.',
                                conversation=conversations.wolf_conv)

available_characters = {
    'self': player,
    'wolf': test_wolf
}





