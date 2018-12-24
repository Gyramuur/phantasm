import functions


class ConversationBranch:
    def __init__(self, name='', prompt='', response='', leads_to='', effect='continue', initiated=False):
        self.name = name
        self.prompt = prompt
        self.response = response
        self.leads_to = leads_to
        self.effect = effect
        self.initiated = initiated


class Conversation:
    def __init__(self, initial_conversation=None, conversation=None, intro='', return_greeting='', has_met=False, in_conversation=False):
        self.initial_conversation = initial_conversation
        self.conversation = conversation
        self.intro = intro
        self.return_greeting = return_greeting
        self.has_met = has_met
        self.in_conversation = in_conversation

    def goodbye(self):
        self.in_conversation = False

    def meet(self):
        self.has_met = True

    def do_effect(self, topic):
        if 'has_met' in topic.effect:
            self.meet()
        elif 'goodbye' in topic.effect:
            self.goodbye()

    def converse(self, widget, player_choice):
        conversation_text = ''

        if not self.has_met:
            conversation_text = conversation_text + self.intro
        else:
            conversation_text = conversation_text + self.return_greeting

        count = 1
        if self.conversation is not None:
            for item in self.conversation:
                conversation_text = conversation_text + f"\n  {count}) {item.prompt}"
                count += 1
                # Probably stuff here.

            functions.update_description(widget, conversation_text)
            '''
            # Deep experimentation.
            if self.initiated:

                selection = widget.ids.text_input.text

            else:

                return'''

            selection = player_choice

            try:
                print(f"Selection is {selection}")
                selection = int(selection) - 1
            except ValueError:

                message = "Enter a number!"
                count = 1
                functions.update_description(widget, message)
                return

            try:
                topic = self.conversation[selection]
                self.do_effect(topic)
                message = topic.response
                self.conversation = functions.get_stage(topic, available_conversations)
                functions.update_description(widget, conversation_text)
                count = 1
            except TypeError:
                message = "That's not a valid choice."
                count = 1
                functions.update_description(widget, message)
                return

        # Maybe have the "in conversation" checks in here



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
