import decorator

class Fighting(decorator.Decorator):
  def abilities(self):
    """Increments the Fighting ability of the character by 1"""
    abilities = super().abilities()
    for ability in abilities:
      if ability[0] == "Fighting":
          ability[1] += 1  # Increment the level of Fighting
    return abilities

  def constitution(self):
    """Adds skill points to the constitution of the character for the Fighting ability"""
    return super().constitution() + 2

  def strength(self):
    """Adds skill points to the strength of the character for the Fighting ability"""
    return super().strength() + 2

  def wisdom(self):
    """Adds skill points to the wisdom of the character for the Fighting ability"""
    return super().wisdom() - 3
