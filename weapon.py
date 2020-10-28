# Weapon Class
class Weapon():
    def __init__(self, name, minDmg, maxDmg, gold):
        self.name = name
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.gold = gold

    def __repr__(self):
        return "{}".format(self.name)