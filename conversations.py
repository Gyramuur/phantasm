class Conversation():
    def __init__(self, current_topics=None, responses=None, next_topics=None):
        if responses is None:
            responses = {}
        self.current_topics = current_topics
        self.responses = responses
        self.next_topic = next_topics

    def list_topics(self):
        # Won't work as is, but just sketching out an idea.
        choice_num = 1
        for topic in self.current_topics:
            print(f"({choice_num}): {topic}")

        choice = input("> ")
        try:
            choice = int(choice)
        except TypeError:
            print("Enter a number!")

        response = self.current_topics[choice - 1]

    # Method to set c_topic via next topic depending on response chosen?


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
    'hello': 'Greet the wolf.',
    'goodbye': 'Leave the conversation.'
}

wolf_start = {
    'hello': 'The wolf wags his tail.',
    'goodbye': 'This will quit the conversation.'
}


wolf_init = Conversation(c_topics=wolf_player_start,
                         responses=wolf_start)
