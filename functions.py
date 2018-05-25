from tkinter import *


def update_description(description, choice, game_text):
    new_description = (f"\n> {choice}" + "\n" + description)
    game_text.insert(END, new_description)
    game_text.see('end')


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
