# class super Hero

from class_game.hero import Hero


class SuperHero(Hero):
    """Creation Super Hero"""

    def __init__(self, name, role, level, century):
        """initiate our hero"""
        super().__init__(name, role, level)
        self.century = century
        self.magic = 100

    def print_hero(self):
         """print out hero"""
         our_hero = ("Name: " + self.name + "\nLevel: " + str(self.level) + "\nRole: " + self.role + "\nCentury: " + self.century + "\nMagic: " + str(self.magic))
         print(our_hero)
