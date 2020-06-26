import random


class Hero(object):

    def __init__(self, initiative=None, name='Hero', hit_points=0, lives=1, weapon=None, level=0):
        """

        :param initiative: order in initiative during an encounter
        :param name: name of hero
        :param hit_points: number of hit points
        :param lives: number of lives
        :param weapon: hero's weapon
        :param level: hero level, important if intiative is tied
        """
        self.name = name
        self.level = level
        self.hit_points = hit_points
        self.max_hit_points = hit_points
        self.lives = lives
        self.alive = True
        self.weapon = weapon
        self.weapon_bonus = 0
        self.initiative = initiative

    def take_damage(self, damage):
        """
        take damage method, activates during enocunter
        :param damage: damage points taken by opponents attack
        :return:
        """
        remaining_points = self.hit_points - damage
        if remaining_points > 0:
            self.hit_points = remaining_points
            print('{} took {} points damage and have {} left'.format(self.name, damage, self.hit_points))
        else:
            print('{} took {} points of damage'.format(self.name, damage))
            self.lives -= 1
            if self.lives > 0:
                self.hit_points = self.max_hit_points
                print('{0.name} lost a life'.format(self))
            else:
                print('{0.name} is dead'.format(self))
                self.alive = False

    def attack(self):
        """
        attack your opponent
        :return: damage points given to opponent
        """
        if self.alive:
            damage = random.randint(1, 6) + self.weapon_bonus
        else:
            damage = 0
        return damage

    def __str__(self):
        return 'Name: {0.name}, lives: {0.lives}, hit points {0.hit_points}, alive: {0.alive}'.format(self)


class Paladin(Hero):

    def __init__(self, name):
        """

        :param name: same as super
        """
        super().__init__(name=name, hit_points=15, lives=1, weapon='Long Sword')
        self.weapon_bonus = 2
        self.spells = 3
        self.level = 2

    def channel_divinity(self):
        """
        can block opponent attack 1/5 of time
        :return: block = true or false
        """
        if random.randint(1, 5) == 5:
            print('{0.name} channeled divinity and blocked the attack'.format(self))
            return True
        else:
            return False

    def heal(self):
        """
        heals hero if spell slots are above 0
        :return:
        """
        inp = input('would you like to heal? y/n')

        if self.spells > 0 and inp == 'y':
            heal = random.randint(1, self.max_hit_points)
            self.hit_points += heal
            print('{0.name} healed for {1} points before the attack!'.format(self, heal))
            self.spells -= 1
        elif self.spells == 0 and inp == 'y':
            print('not enough spells!')
            pass
        else:
            pass

    def take_damage(self, damage):
        """
        take damage in encounter
        :param damage: damage points taken
        :return:
        """
        if self.channel_divinity():
            pass
        else:
            if damage > self.hit_points:
                self.heal()
            super().take_damage(damage=damage)

    def battle_cry(self):
        """
        something fun to yell when hacking apart an enemy
        :return:
        """
        print('Taste my blade!')

    def attack(self):
        """
        attack with weapon
        :return: damage dealt to opponent
        """
        inp = input('attack? y/n')
        if inp == 'y':
            self.battle_cry()
            damage = super().attack()
        else:
            print('I\'m a little lazy and not going to attack today')
            damage = 0

        return damage


class Wizard(Hero):

    def __init__(self, name):
        """
        wizard hero, can use spells as attacks
        :param name:
        """
        super().__init__(weapon='Dagger', hit_points=24)
        self.name = name
        self.lives = 1
        self.weapon_bonus = -1
        self.spells = 10

    def attack(self):
        """
        can choose to attack with spells or dagger but beware, the wizard's dagger is -1 to all attacks
        :return: damage points
        """
        attack_type = random.randint(1, 5)

        inp = input('spell attack? y/n')

        if self.spells > 0 and inp == 'y':

            if attack_type == 1:
                print('Taste my frosty ray!')
                damage = random.randint(1, 6)
            elif attack_type == 2:
                print('Eat fire!')
                damage = random.randint(1, 8)
            elif attack_type == 3:
                print('Zappo!')
                damage = random.randint(1, 9)
            elif attack_type == 4:
                print('Look out for my Beam of Spikey Hedgehogs!!')
                damage = random.randint(1, 10)
            else:
                print('Abraca-DEAD!')
                damage = random.randint(1, 40)

            self.spells -= 1
        elif inp == 'n':
            damage = super().attack()
        else:
            print('OOOOH NOOOOO, I\'m out of spellz')
            damage = super().attack()

        return damage

    def heal(self):
        """
        burn a spell slot to heal yourself before a death blow
        :return:
        """
        inp = input('would you like to heal? y/n')

        if self.spells > 0 and inp == 'y':
            heal = random.randint(1, self.max_hit_points)
            self.hit_points += heal
            print('{0.name} healed for {1} points before the attack!'.format(self, heal))
            self.spells -= 1
        elif self.spells == 0 and inp == 'y':
            print('not enough spells!')
            pass
        else:
            pass

    def take_damage(self, damage):
        """
        take damage
        :param damage: damage points dealt by opponent
        :return:
        """
        if damage > self.hit_points:
            self.heal()
        super().take_damage(damage=damage)

    def __str__(self):
        """
        basic info about class instance
        :return: string of info
        """
        return 'Name: {0.name}, lives: {0.lives}, hit points {0.hit_points}, alive: {0.alive}'.format(self)
