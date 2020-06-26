import random


class Enemy(object):
    """
    basic class for enemy
    """

    def __init__(self, initiative=None, name='Enemy', hit_points=0, lives=1, level=0):
        """

        :param initiative: order in encounter
        :param name: name of character
        :param hit_points: total hit points
        :param lives: number of lives
        :param level: level, important for initiative order
        """
        self.name = name
        self.hit_points = hit_points
        self.max_hit_points = hit_points
        self.lives = lives
        self.alive = True
        self.level = level
        self.weapon_bonus = 0
        self.armour_bonus = 0
        self.initiative = initiative
    
    def take_damage(self, damage):
        """
        damage dealt by opponent is subtracted from hit points
        :param damage: damage dealt by opponent
        :return:
        """
        remaining_points = self.hit_points - damage
        if remaining_points > 0:
            self.hit_points = remaining_points
            print('{} took {} points damage and have {} left'.format(self.name, damage, self.hit_points))
        else:
            self.lives -= 1
            print('{} took {} points of damage'.format(self.name, damage))
            if self.lives > 0:
                self.hit_points = self.max_hit_points
                print('{0.name} lost a life'.format(self))
            else:
                print('{0.name} is dead'.format(self))
                self.alive = False

    def attack(self):
        """
        damage to deal to opponents
        :return: damage
        """
        if self.alive:
            damage = random.randint(1, 6) + self.weapon_bonus
        else:
            damage = 0
        return damage

    def __str__(self):
        return 'Name: {0.name}, lives: {0.lives}, hit points {0.hit_points}, alive: {0.alive}'.format(self)


class Troll(Enemy):
    """
    subclass of enemy, added grunt method
    """
    def __init__(self, name):
        """

        :param name: name of troll
        """
        super().__init__(name=name, lives=1, hit_points=30)
        self.weapon_bonus = 1  # because he is very strong
        self.level = 1

    def grunt(self):
        """
        something fun to yell at opponent before clubbing them
        :return:
        """
        print('Me {0.name}, {0.name} stomp you'.format(self))

    def attack(self):
        """
        always grunt before attack
        :return:
        """
        self.grunt()
        return super().attack()


class Vampyre(Enemy):

    """
    another subclass of enemy which can dodge and avoid damage
    """

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        """
        dodges attack if random.randint == 3
        :return: True or False if attack is dodged
        """
        if random.randint(1, 3) == 3:
            print('{0.name} dodges the attack'.format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        """
        inherited from enemy class, doesn't take damage if dodge was successfull
        :param damage: damage points dealt by opponent
        :return:
        """
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):
    """
    king of the baddies, subclass of Vampyre

    can dodge and only takes 1/4 damage
    """
    def __init__(self, name):
        super().__init__(name=name)
        self.hit_points = 50
        self.lives = 3

    def take_damage(self, damage):
        """
        takes 1/4 damage
        :param damage: damage dealt by opponent
        :return:
        """
        super().take_damage(damage=damage//4)



