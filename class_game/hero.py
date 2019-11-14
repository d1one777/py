# class Hero

class Hero ():
    """class Hero"""
    def __init__(self, name, role, level):
        """initiate our hero"""
        self.name = name
        self.level = level
        self.role = role

    def print_hero(self):
         """print out hero"""
         our_hero = ("Name: " + self.name + "\nLevel: " + str(self.level) + "\nRole: " + self.role )
         print(our_hero)

    def write_hero(self):
         """print out hero"""
         our_hero = ("Name: " + self.name + "\nLevel: " + str(self.level) + "\nRole: " + self.role )
         return (our_hero)

    def level_up(self):
         """upgreat hero"""
         self.level += 1

    def fight (self):
         print("Hero" + self.name + "-= start fight =-")


