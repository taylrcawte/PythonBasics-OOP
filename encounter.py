import random


class Fight(object):
    """
    sets up env for fight to occur b

    fight can only occur between 2 players at a time

    first the order of attack is established, then players take turns attacking eachother until one is dead
    """

    def __init__(self, player1, player2, order=None):
        self.player1 = player1
        self.player2 = player2
        self.order = order

    def initative_order(self):
        """
        determines initiative order

        if 2 players roll the same initiative, preference is given to higher level
        :return:
        """
        self.player1.initiative = random.randint(0, 20)
        self.player2.initiative = random.randint(0, 20)
        print()

        if self.player1.initiative == self.player2.initiative:
            print('Well, well, these foes are well matched but ...')
            if self.player1.level > self.player2.level:
                print('Player 1 is much more intimidating and has the advantage!')
                self.order = [self.player1, self.player2]
            else:
                print('Player 2 is much more intimidating and has the advangtage!')
                self.order = [self.player2, self.player1]
        else:
            if self.player1.initiative > self.player2.initiative:
                print('{0.name} is much quicker! {0.name} attacks first!'.format(self.player1))
                self.order = [self.player1, self.player2]
            else:
                print('{0.name} is much quicker! {0.name} attacks first!'.format(self.player2))
                self.order = [self.player2, self.player1]

        return self.order

    def fight(self):
        """
        fight to the death! 2 players take turns attacking until 1 is declared the victor

        :return:
        """

        while True:

            self.order[1].take_damage(self.order[0].attack())
            if not self.order[1].alive:
                break

            self.order[0].take_damage(self.order[1].attack())
            if not self.order[0].alive:
                break

        winner = self.order[0] if self.order[0].alive else self.order[1]
        loser = self.order[1] if not self.order[1].alive else self.order[0]

        print()
        print('{0.name} is victorious! {1.name} will be plundered and they bring shame on their house'.format(
            winner, loser))
