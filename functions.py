

def update_description(widget, description):
    new_description = f"{widget.ids.game_label.game_text}\n > {widget.ids.text_input.text}\n" \
                        f"{description}\n"

    widget.ids.game_label.game_text = new_description


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


def get_stage(topic, available_conversations):
    if topic.leads_to in available_conversations:
        return available_conversations[topic.leads_to]
