import random
from stylecss import *


class Figure:
    def __init__(self, health, damage, defensiv, name):
        self.health = health
        self.damage = damage
        self.defensiv = defensiv
        self.name = name

    def attack(self, other):
        damage = self.damage - other.defensiv
        if damage > 0.0:
            other.health = other.health - damage


# Player am Anfang vom Spiel eingeben des Namens, eventuell eingeben einer Wunschwaffe einer Auswahl, Funktionen:
# attack, going, ...

class Player(Figure):
    inventory = []

    def __init__(self, name):
        super().__init__(10, 0.5, 6.0, name)


# Enemy Klasse, Health random, damage random, defensiv random, name aus Liste von Namen, die vorher definiert wird,
# Funktionen attack, soll random auf der Map auftauchen, inventory zum Plündern?

class Enemy(Figure):
    inventory = []

    def __init__(self, health, damage, defensiv):
        name = random.choice(["Kral", "Myamir", "Peter", "Rixus", "Zira", "Naro", "Whispess", "Weavess", "Brewess",
                              "Darth Vader", "Nemesis", "Bowser", "Venom", "Dr. Eggman", "Voldemort", "Ridley",
                              "Sauron", "Ultron", 'Diablo', "Magneto", "Pimmelberger", "Thanos", "Jigsaw",
                              "Leatherface", "Palpatine", "Pennywise", "Thomas die Lokomotive"])
        super().__init__(self, health, damage, defensiv, name)
