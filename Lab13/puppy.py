import stateasleep
import stateeat
import stateplay

class Puppy:
  def __init__(self):
    """
    Initialize a Puppy object.
    The puppy starts in the 'asleep' state by default.
    """
    self._state = stateasleep.StateAsleep()
    self._feeds = 0
    self._plays = 0

  @property
  def feeds(self):
    """
    Get the number of times the puppy has been fed.
    Returns:
        int: The number of times the puppy has been fed.
    """
    return self._feeds

  @property
  def plays(self):
    """
    Get the number of times the puppy has played.
    Returns:
        int: The number of times the puppy has played.
    """
    return self._plays

  def change_state(self, new_state):
    """
    Change the state of the puppy.
    Args:
        new_state (object): The new state of the puppy.
    """
    self._state = new_state

  def throw_ball(self):
    """
    Make the puppy play by throwing a ball.
    Returns:
        str: The result of the play action.
    """
    return self._state.play(self)
      
  def give_food(self):
    """
    Feed the puppy.
    Returns:
        str: The result of the feeding action.
    """
    return self._state.feed(self)
    
  def inc_feeds(self):
    """
    Increment the count of feeds by 1.
    """
    self._feeds += 1
    
  def inc_plays(self):
    """
    Increment the count of plays by 1.
    """
    self._plays += 1
    
  def reset(self):
    """
    Reset the counts of feeds and plays to zero.
    """
    self._feeds = 0
    self._plays = 0
