import decorator

class Archery(decorator.Decorator):
  def abilities(self):
    """Increments the Archery ability of the character by 1"""
    abilities = super().abilities()
    for ability in abilities:
      if ability[0] == "Archery":
          ability[1] += 1  # Increment the level of Archery
    return abilities

  def constitution(self):
    """Adds skill points to the constitution of the character for the Archer ability"""
    return super().constitution() - 2

  def strength(self):
    """Adds skill points to the strength of the character for the Archer ability"""
    return super().strength() + 5

  def wisdom(self):
    """Adds skill points to the wisdom of the character for the Archer ability"""
    return super().wisdom() - 2

