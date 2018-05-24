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

available_items = {
    'orb': test_item,
    'cube': test_item2,
    'statue': heavy_test
}


