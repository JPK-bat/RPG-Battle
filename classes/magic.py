import random


class spell:
    def __init__(self,name,cost,damage,type):
        self.name=name
        self.cost=cost
        self.damage=damage
        self.type=type

    def generate_spelldamage(self):
        low=self.damage-5
        high=self.damage+10
        return random.randrange(low,high)