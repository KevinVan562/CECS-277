import puppystate
import stateasleep
import stateplay

class StateEat(puppystate.PuppyState):
  def feed(self, puppy):
    """
    Feed the puppy and potentially transition its state.
    Args:
        puppy (Puppy): The Puppy object being fed.
    Returns:
        str: A message indicating the result of the feeding action.
    """
    puppy.inc_feeds()
    if puppy.feeds < 3:
      return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    else:
      puppy.change_state(stateasleep.StateAsleep())
      return "The puppy continues to eat as you add another scoop of kibble to its bowl. \nThe puppy ate so much it fell asleep!"
      
  def play(self, puppy):
    """
    Attempt to play with the puppy while it is eating.
    Args:
        puppy (Puppy): The Puppy object being interacted with.
    Returns:
        str: A message indicating the result of the play action.
    """
    puppy.inc_plays()
    puppy.change_state(stateplay.StatePlay())
    return "The puppy looks up from its food and chases the ball you threw."
