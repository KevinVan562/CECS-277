import die


class Player:
    def __init__(self):
        """Initializes the player's points to 0 and creates a list of three Die objects"""
        self.points = 0
        self.dice = [die.Die(), die.Die(), die.Die()]

    def get_points(self):
        """Returns the total points"""
        return self.points

    def roll_dice(self):
        """Rolls each of the three dice in the list and sorts them"""
        for d in self.dice:
            d.roll()
        self.dice.sort()

    def has_pair(self):
        """Returns True if two dice in the list have the same value and increments the player's points by 1"""
        if self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2]:
            self.points += 1
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        """Rerurns True if all three dice in the list have the same value and increments the player's points by 3"""
        if self.dice[0] == self.dice[1] == self.dice[2]:
            self.points += 3
            return True
        else:
            return False

    def has_series(self):
        """Returns True if the values of each of the dice in the list are in a sequence and increments the player's points by"""
        if self.dice[1] - self.dice[0] == 1 and self.dice[2] - self.dice[1] == 1:
            self.points += 2
            return True

    def __str__(self):
        """Returns a string in the format: D1=2, D2=4, D3=6"""
        return "D1=" + str(self.dice[0]) + " D2=" + str(self.dice[1]) + " D3=" + str(self.dice[2])
