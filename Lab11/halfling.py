import character

class Halfling(character.Character):
  def __init__(self, n):
    """Initializes the Elf character with a name"""
    super().__init__(n + " the Halfling")

  def abilities(self):
    """Initializes the Elf character with a name"""
    return [["Archery", 0], ["Fighting", 0], ["Fire", 0], ["Healing", 1]]

  def constitution(self):
    """Returns the constitution level of the character"""
    return 15

  def strength(self):
    """Returns the strength level of the character"""
    return 10

  def wisdom(self):
    """Returns the wisdom level of the character"""
    return 13
