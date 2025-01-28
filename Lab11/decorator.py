import character
import abc

class Decorator(character.Character, abc.ABC):
  def __init__(self, c):
    """Initializes the decorator with the character to be created"""
    super().__init__(c.name)
    self._char = c

  def abilities(self):
    """Returns the abilities of the character"""
    return self._char.abilities()

  def constitution(self):
    """Returns the constitution of the character"""
    return self._char.constitution()

  def strength(self):
    """Returns the strength of the character"""
    return self._char.strength()

  def wisdom(self):
    """Returns the wisdom of the character"""
    return self._char.wisdom()
