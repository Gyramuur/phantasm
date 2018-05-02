class Conversation():
    def __init__(self, conversation_name, id_chart):
        self.conversation_name = conversation_name
        self.id_chart = id_chart  # Don't know if I need this.


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

dialogue_lookup = {
    'wolf_talked_to': wolf_start,
    'wolf_greeted': wolf_greeted
}
