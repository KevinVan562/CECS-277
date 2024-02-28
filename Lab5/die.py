import random


class Die:
    """Represents a single Die which is 6-sided 
    Attributes:
      sides (int): number of sides on the die
      value (int): value of the die)
    """

    def __init__(self, sides=6):
        """Initializes the die with the number of sides and value """
        self.sides = sides
        self.value = self.roll()

    def roll(self):
        """Rolls the dice and returns the value"""
        self.value = random.randint(1, self.sides)
        return self.value

    def __str__(self):
        """Represents the die as a string"""
        return str(self.value)

    def __lt__(self, other):
        """Check if value of die is less than other"""
        return self.value < other.value

    def __eq__(self, other):
        """Check if value of die is equal to other"""
        return self.value == other.value

    def __sub__(self, other):
        """Subtracts the value of the die from other"""
        return self.value - other.value
