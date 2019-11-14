# main game

from class_game.hero import Hero
from class_game.superhero import SuperHero

# main

# inputfile = "heroes.txt"
outputfile = "myheroes.txt"
myfile2 = open(outputfile, mode='w', encoding='latin_1')

hero1 = Hero("Usyk", "boxer", 20)
hero2 = Hero("Busyk", "boxer", 28)
hero3 = SuperHero("Jocker", "boxer", 30, "IX")

hero1.print_hero()
myfile2.write(hero1.write_hero())
print("-----")
myfile2.write("\n-----")
hero2.print_hero()
hero3.print_hero()

myfile2.close()

