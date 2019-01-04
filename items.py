import classes

test_item = classes.Item(
    name='mysterious orb',
    desc='A strange orb that is slowly pulsing, alternating between hues of lavender and cerulean.',
    value=1000
)

test_item2 = classes.Item(
    name='cube',
    desc="It's a cube! Or maybe it's a tesseract?",
    value=1000
)

heavy_test = classes.Item(
    name='statue of the night goddess',
    desc='A tall statue of the night goddess, carved from white marble.',
    value=10000,
    weight=10000
)

apple = classes.Item(
    name='apple',
    desc='A red, delicious looking apple.',
    value=2,
    weight=1
)

stick = classes.Item(
    name='stick',
    desc='A prosaic-looking stick.',
    value=0,
    weight=1
)

bread = classes.Item(
    name='bread',
    desc='That\'s some white bread.',
    value=2,
    weight=1
)

chest = classes.Item(
    name='oak chest',
    desc='A chest made of oak-wood.',
    value=20,
    weight=500,
    container=True
)


available_items = {
    'orb': test_item,
    'cube': test_item2,
    'statue': heavy_test,
    'stick': stick,
    'apple': apple,
    'chest': chest,
    'bread': bread
}

common_items = [stick, apple, bread]


