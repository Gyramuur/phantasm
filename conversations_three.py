class Conversation():
    def __init__(self, id_chart, conversation=None, intro='', return_greeting='', has_met=False, disposition=0):
        if conversation is None:
            conversation = {}
        self.conversation = conversation
        self.intro = intro
        self.return_greeting = return_greeting
        self.id_chart = id_chart  # Don't know if I need this.
        self.has_met = has_met
        self.disposition = disposition

    # You need 'conversation levels', as in, different parts of the conversation that link to other parts.
    # So start has certain responses that lead to other levels.

    def converse(self):
        if not self.has_met:
            print(self.intro)
        else:
            print(self.return_greeting)

        count = 1
        while True:
            for topic in self.conversation['level']:
                print(f"{count}: {topic['choice_name']}")
                count += 1
            # Probably stuff here.
            choice = input('> ')

            # Stuff here about looking at the choice number and matching it up to which topic is displayed.


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
                         return_greeeting='The wolf barks and wags his tail excitedly.')
