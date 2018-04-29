class Item():
    def __init__(self, name='item', desc='', value=1, damage=1, unlocks='', edible=False, container=False,
                 capacity=0, weight=1):
        self.name = name
        self.desc = desc
        self.value = value
        self.damage = damage
        self.unlocks = unlocks
        self.edible = edible
        self.container = container
        self.capacity = capacity
        self.weight = weight

    def item_desc(self):
        print(self.desc)
        print(f"It is worth: {self.value} gold.")
        print(f"It weighs {self.weight} pounds.")
        print(f"It does {self.damage} damage.")


