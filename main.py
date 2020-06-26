"""
short game to showcase basics of inheritance and composiition in object oriented python!

choose actions as the hero to defeat trolls vampires, and even a vampire king!
"""

from enemy import Enemy, Troll, Vampyre, VampyreKing
from Hero import Paladin, Wizard
from encounter import Fight


if __name__ == '__main__':
    Mr_Peanut = Paladin('Mr. Peanut, The Emancipator')
    Steve = Wizard('The Fantastic Steve')
    Blorgnar = Troll('Blorgnar')
    Glorbnar = Troll('Glorbnar')
    SirSuck = VampyreKing('Sir Suck')

    encounter = Fight(Mr_Peanut, Blorgnar)
    encounter.initative_order()
    encounter.fight()

    encounter2 = Fight(Steve, Glorbnar)
    encounter2.initative_order()
    encounter2.fight()
