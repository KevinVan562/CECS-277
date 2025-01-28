import decorator

class Healing(decorator.Decorator):
  def abilities(self):
    """Increments the Healing ability of the character by 1"""
    abilities = super().abilities()
    for ability in abilities:
      if ability[0] == "Healing":
          ability[1] += 1  # Increment the level of Healing
    return abilities

  def constitution(self):
    """Adds skill points to the constitution of the character for the Healing ability"""
    return super().constitution() + 3

  def strength(self):
    """Adds skill points to the strength of the character for the Healing ability"""
    return super().strength() - 4

  def wisdom(self):
    """Adds skill points to the wisdom of the character for the Healing ability"""
    return super().wisdom() + 2
