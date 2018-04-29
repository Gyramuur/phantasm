def get_target(choice, available_items, available_characters):
    choice = choice.split()

    for word in choice:
        if word in available_items:
            return available_items[word]

        else:
            continue

    for word in choice:
        if word in available_characters:
            return available_characters[word]

        else:
            continue

        # return item


def get_direction(choice):

    directions = ['north', 'south', 'west', 'east', 'inside', 'outside', 'upstairs', 'downstairs']

    choice = choice.split()
    for word in choice:
        if word in directions:
            return word
        else:
            continue
