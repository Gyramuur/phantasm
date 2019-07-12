import functions
import characters

class ConversationBranch:
    def __init__(self, name='', prompt='', response='', leads_to='', effect='continue', initiated=False):
        self.name = name
        self.prompt = prompt
        self.response = response
        self.leads_to = leads_to
        self.effect = effect
        self.initiated = initiated


class Conversation:
    def __init__(self, initial_conversation=None, conversation=None, intro='', return_greeting='', has_met=False,
                 in_conversation=False):
        self.initial_conversation = initial_conversation
        self.conversation = conversation
        self.intro = intro
        self.return_greeting = return_greeting
        self.has_met = has_met
        self.in_conversation = in_conversation

    def goodbye(self):
        self.in_conversation = False
        characters.player.target = None
        print("Conversation exited, supposedly.")
        return

    def meet(self):
        self.has_met = True

    def do_effect(self, topic):
        if topic.effect == 'goodbye':
            self.goodbye()

    def converse(self, widget, player_choice):

        print(f"Conversing with player selection as {player_choice}.")
        # Checks
        self.in_conversation = True
        conversation_text = ''

        if "talk" in player_choice:
            if not self.has_met:
                print("Hasn't met.")
                conversation_text = conversation_text + self.intro
                self.has_met = True
            else:
                print("Met.")
                conversation_text = conversation_text + self.return_greeting

            count = 1
            for item in self.conversation:
                conversation_text = conversation_text + f"\n  {count}) {item.prompt}"
                count += 1
                # Probably stuff here.

        try:
            if conversation_text != "":
                functions.update_description(widget, conversation_text)
                print(f"Conversation text updating with {conversation_text}.")

            selection = int(player_choice) - 1

        except ValueError:
            return
        # if 'talk' in selection:
        #    return

        """
        # That's it, I quit.
        try:
            selection = int(selection) - 1
            print(f"Selection is {selection}")
        except ValueError:
            message = "Enter a number!"
            functions.update_description(widget, message)
            return"""

        try:
            topic = self.conversation[selection]
            self.do_effect(topic)
            print(f"Topic is {topic.name}")
            message = topic.response
            self.conversation = functions.get_stage(topic, available_conversations)
            count = 1
            for item in self.conversation:
                message = message + f"\n{count}) {item.prompt}"
                count += 1
            print(f"Updating description with {message}.")
            print(f"Player's choice is {player_choice}.")
            functions.update_description(widget, message)
        except IndexError:
            message = "That's not a valid choice."
            functions.update_description(widget, message)
            return

            # Maybe have the "in conversation" checks in here
            '''
            # Deep experimentation.
            if self.initiated:

                selection = widget.ids.text_input.text

            else:

                return'''


wolf_greet = ConversationBranch(
    name='wolf_greet',
    prompt='(Greet the wolf.)',
    response='The wolf barks at you and wags his tail.',
    leads_to='wolf_stage_greeted',
    effect='has_met'
)

wolf_insult = ConversationBranch(
    name='wolf_insult',
    prompt='(Shake your fist and yell at the wolf!)',
    response='The wolf growls and barks at you!',  # Should set up disposition.
    effect='goodbye'  # You need multiple effects to change the disposition as well as leave the conversation.
    # ^ We are nowhere near achieving disposition yet, my dude.
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
    leads_to='wolf_stage_goodboy',
    response='The wolf smiles and wags his tail. "I am!" he barks.',
)

wolf_can_talk = ConversationBranch(
    name='wolf_can_talk',
    prompt='"Whoah! You can talk?"',
    leads_to='wolf_stage_talk',
    response='The wolf grins, taking a seat. "Of course I can. What do you mistake me for?"',)

wolf_pretend = ConversationBranch(
    name='wolf_pretend',
    prompt='''"I...am going to pretend I didn't just hear you speak."''',
    response='The wolf tilts his head at you. "Is that so surprising?" he asks.')

wolf_see_later = ConversationBranch(
    name='wolf_see_later',
    prompt='''"Okay. I guess I'll see you later, then.''',
    response='"Of course," the wolf says."',
    effect='goodbye')

wolf_stage_start = [wolf_greet, wolf_goodbye]
wolf_stage_greeted = [wolf_goodboy, wolf_insult, wolf_goodbye]
wolf_stage_goodboy = [wolf_can_talk, wolf_pretend, wolf_goodbye]
wolf_stage_talk = [wolf_see_later]

available_conversations = {
    'wolf_stage_start': wolf_stage_start,
    'wolf_stage_greeted': wolf_stage_greeted,
    'wolf_stage_goodboy': wolf_stage_goodboy,
    'wolf_stage_talk': wolf_stage_talk
}


wolf_conv = Conversation(
    intro="The wolf looks up at you curiously.",
    conversation=wolf_stage_start,
    return_greeting='The wolf smiles at you.'
)
