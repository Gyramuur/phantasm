def wolf_greet():
    print("He wags his tail happily.")


def wolf_conversation():
    wolf_start = ['1. [Greet the wolf.]',
                  '2. [Leave.]']

    for topic in wolf_start:
        print(topic)

    choice = input("> ")
    if choice == '1':
        wolf_greet()
    else:
        print("You walk away.")
        return None

