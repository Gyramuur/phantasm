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


'''
def conversation(choice, available_characters):
    return
    # Do a get_target on characters and load conversation based on that. It has to work the same NO MATTER which
    # character, but has to be unique for every character. Maybe a class?'''


# Think we got it here. We just need to write some code in the conversations class now to switch self.conversation.
def get_stage(topic, available_conversations):
    if topic.leads_to in available_conversations:
        return available_conversations[topic.leads_to]
