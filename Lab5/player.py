import die


class Player:
    def __init__(self):
        self.points = 0
        self.dice = [die.Die(), die.Die(), die.Die()]
        self.dice_values = [d.roll() for d in self.dice]
        self.dice.sort()

    def get_points(self):
        return self.points

    def roll_dice(self):
        self.dice_values = [d.roll() for d in self.dice]
        self.dice.sort()

    def has_pair(self):
        if self.dice_values[0] == self.dice_values[1] or self.dice_values[1] == self.dice_values[2] or self.dice_values[0] == self.dice_values[2]:
            self.points += 1
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        if self.dice_values[0] == self.dice_values[1] and self.dice_values[1] == self.dice_values[2]:
            self.points += 3
            return True
        else:
            return False

    def has_series(self):
        if self.dice_values[2] - self.dice_values[1] == 1 and self.dice_values[1] - self.dice_values[0] == 1:
            self.points += 2
            return True
        else:
            return False

    def __str__(self):
        return f"D1={self.dice_values[0]}, D2={self.dice_values[1]}, D3={self.dice_values[2]}"
