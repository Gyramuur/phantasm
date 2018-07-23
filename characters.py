import classes
import conversations

test_wolf = classes.Entity(name='Wolf',
                                desc='A large gray wolf. He looks happy.',
                                conversation=conversations.wolf_conv)

player = classes.Player(name='Scintilla',
                        target=test_wolf)

available_characters = {
    'self': player,
    'wolf': test_wolf
}





