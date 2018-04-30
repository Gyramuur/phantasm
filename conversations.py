class Conversation():
    def __init__(self, c_topic=None, responses=None, next_topic=None):
        if responses is None:
            responses = {}
        self.c_topic = c_topic
        self.responses = responses
        self.next_topic = next_topic
