import phantasm_functions as funcs


class ConversationBranch:
    def __init__(self, name='', prompt='', response='', leads_to='', effect='continue'):
        self.name = name
        self.prompt = prompt
        self.response = response
        self.leads_to = leads_to
        self.effect = effect


class Conversation:
    def __init__(self, initial_conversation=None, conversation=None, intro='', return_greeting='', has_met=False, in_conversation=True):
        self.initial_conversation = initial_conversation
        self.conversation = conversation
        self.intro = intro
        self.return_greeting = return_greeting
        self.has_met = has_met
        self.in_conversation = in_conversation

    # You need 'conversation levels', as in, different parts of the conversation that link to other parts.
    # So start has certain responses that lead to other levels.

    def goodbye(self):
        self.in_conversation = False

    def meet(self):
        self.has_met = True

    def do_effect(self, topic):
        if topic.effect == 'has_met':
            self.meet()

    def converse(self):

        self.in_conversation = True
        self.conversation = self.initial_conversation

        if not self.has_met:
            print(self.intro)
        else:
            print(self.return_greeting)

        count = 1
        while self.in_conversation:
            # print(self.conversation)

            if self.conversation is not None:
                for item in self.conversation:
                    print(f"{count}: {item.prompt}")
                    count += 1
                    # Probably stuff here.
                choice = input('> ')

                try:
                    selection = int(choice) - 1
                except ValueError:
                    print("Enter a number!")
                    count = 1
                    continue

                try:
                    topic = self.conversation[selection]
                    self.do_effect(topic)
                    print(topic.response)
                    self.conversation = funcs.get_stage(topic, available_conversations)
                    count = 1
                except IndexError:
                    print("That's not a valid choice.")
                    count = 1
                    continue

            else:
                self.goodbye()

            # Stuff here about looking at the choice number and matching it up to which topic is displayed.

# Lookup table for conversation stages which they lead to.

# You could probably take out the whole conversation dictionary thing, remove the 'level' (the start seen here),

# Or have the conversation link to a class.

# You might still need levels tho. Perhaps as part of the Conversation class?


wolf_greet = ConversationBranch(
    name='wolf_greet',
    prompt='(Greet the wolf.)',
    response='The wolf barks at you and wags his tail.',
    leads_to='wolf_stage_greeted',
    effect='has_met'
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
    response='The wolf smiles and wags his tail.',
    effect='goodbye'
)

wolf_insult = ConversationBranch(
    name='wolf_insult',
    prompt='(Shake your fist and yell at the wolf!)',
    response='The wolf growls and barks at you!',  # Should set up disposition.
    effect='goodbye'  # You need multiple effects to change the disposition as well as leave the conversation.
)

wolf_stage_start = [wolf_greet, wolf_goodbye]
wolf_stage_greeted = [wolf_goodboy, wolf_insult, wolf_goodbye]

available_conversations = {
    'wolf_stage_start': wolf_stage_start,
    'wolf_stage_greeted': wolf_stage_greeted
}


wolf_conv = Conversation(
    intro="The wolf looks up at you curiously.",
    initial_conversation=wolf_stage_start,
    conversation=wolf_stage_start,
    return_greeting='The wolf smiles at you.'
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
