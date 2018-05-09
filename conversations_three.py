class ConversationBranch:
    def __init__(self, name='', prompt='', response='', leads_to='', effect=''):
        self.name = name
        self.prompt = prompt
        self.response = response
        self.leads_to = leads_to
        self.effect = effect


class Conversation:
    def __init__(self, conversation=None, intro='', return_greeting='', has_met=False):
        if conversation is None:
            conversation = {}
        self.conversation = conversation
        self.intro = intro
        self.return_greeting = return_greeting
        self.has_met = has_met

    # You need 'conversation levels', as in, different parts of the conversation that link to other parts.
    # So start has certain responses that lead to other levels.

    def converse(self):

        if not self.has_met:
            print(self.intro)
        else:
            print(self.return_greeting)

        count = 1
        while True:
            for v in self.conversation['topics'].values():  # How the fuck do you do it? Get the level
                # and set it somehow, maybe?
                print(f"{count}: {v.prompt}")
                count += 1
            # Probably stuff here.
            choice = input('> ')

            try:
                selection = int(choice) - 1
            except TypeError:
                print("Enter a number!")
                continue

            try:
                value = list(self.conversation['topics'].values())[selection]
                print(value.response)
            except IndexError:
                print("That's not a valid choice.")
                continue

            # Stuff here about looking at the choice number and matching it up to which topic is displayed.

# Lookup table for conversation stages which they lead to.

# You could probably take out the whole conversation dictionary thing, remove the 'level' (the start seen here),

# Or have the conversation link to a class.

# You might still need levels tho. Perhaps as part of the Conversation class?


wolf_greet = ConversationBranch(
    name='wolf_greet',
    prompt='(Greet the wolf.)',
    response='The wolf barks at you and wags his tail.',
    leads_to='wolf_goodboy'  # Perhaps have a list of prompts, and each one will lead to something different.
)

wolf_goodbye = ConversationBranch(
    name='wolf_goodbye',
    prompt='(Leave.)',
    response='You walk away from the wolf.',
    effect='goodbye'
)

wolf_goodboy = ConversationBranch(
    name='wolf_goodboy',
    prompt='"Who\'s a good boy?"',
    response='The wolf tilts his head curiously.',
    leads_to='something'
)

wolf_conv = Conversation(
    intro="The wolf looks up at you curiously.",
    conversation={
        'topics': {
            'wolf_greet': wolf_greet,
            'wolf_goodbye': wolf_goodbye
        }
    }
)

# Experimental stuff below.
'''
wolf_conversation = Conversation(intro='The wolf looks at you and tilts his head curiously.',
                                 return_greeting='The wolf barks and wags his tail.',
                                 conversation={
                                     'start': {
                                         'hello': {
                                             'prompt': '"Hello there, wolf," you say.',
                                             'leads_to': None,
                                             'effect': None
                                         },
                                         'have_met': 'I don\'t believe we\'ve met.',
                                         'wave': 'You wave at the wolf.',
                                         'goodbye': 'Leave.'
                                     }})


wolf_greeted = {
    'init': 'The wolf seems cordial enough, as far as wolves go.'
}

wolf_start = {
    'hello': 'wolf_greeted',  # Change to name via lookup table.
    'good_boy': 'The wolf barks!',
    'understand': 'He takes a moment to consider that, then nods.',
    'weather': 'The wolf tilts his head curiously.',
    'goodbye': 'You leave.'
}

# Perhaps this can be the table.
dialogue_lookup = {
    'wolf_talked_to': wolf_start,
    'wolf_greeted': wolf_greeted
}

wolf_conv = Conversation(id_chart=wolf_start,
                         intro='The wolf looks at you curiously.',
                         return_greeeting='The wolf barks and wags his tail excitedly.')'''
