class Conversation():
    def __init__(self, current_topics=None, pointers=None):
        if pointers is None:
            pointers = {}
        self.current_topics = current_topics
        self.pointers = pointers

    def list_topics(self):
        # Won't work as is, but just sketching out an idea.
        choice_num = 1
        while True:
            for topic in self.current_topics:
                print(f"({choice_num}): {self.current_topics[topic]}")
                choice_num += 1

            choice = input("> ")

            self.switch_topic(choice, self.pointers)

    def switch_topic(self, choice, pointers):
        self.current_topics = pointers[choice]


wolf_greet01 = """The wolf looks up at you, then, after a moment, mutters a greeting."""
wolf_affirm = """
"Yes," he says somewhat petulantly, "of course I can talk."
"""
wolf_woof = """The wolf barks at you excitedly."""

wolf_conv = {
    'greeting': wolf_greet01,
    'can_talk': wolf_affirm,
    'woof': wolf_woof
}


wolf_player_start = {
    'wolf_hello': 'Greet the wolf.',
    'goodbye': 'Leave the conversation.'
}

wolf_start = {
    'wolf_hello': 'The wolf wags his tail.',
    'goodbye': 'The conversation (does not) end.'
}

wolf_player_greet = {
    'understand': '"Do you understand me?"',
    'good_boy': '"Who\'s a good boy?"',
    'goodbye': 'Leave the conversation.'
}

wolf_greet = {
    'understand': 'He looks at you for a moment, then says, "Yes..."',
    'good_boy': 'The wolf barks excitedly!',
    'goodbye': 'The conversation (does not) end.'
}

wolf_pointers = {
    'wolf_hello': wolf_start['wolf_hello'],
    'wolf_goodbye': wolf_start['goodbye']
}


wolf_init = Conversation(current_topics=wolf_player_start,
                         pointers=wolf_start)
