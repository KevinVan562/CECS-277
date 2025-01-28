import puppystate
import stateeat
import stateplay

class StateAsleep(puppystate.PuppyState):
  def feed(self, puppy):
    """
    Feed the puppy and transition its state.
    Args:
        puppy (Puppy): The Puppy object being fed.
    Returns:
        str: A message indicating the result of the feeding action.
    """
    puppy.inc_feeds()
    puppy.change_state(stateeat.StateEat())
    return "The puppy wakes up and comes running to eat."

  def play(self, puppy):
    """
    Attempt to play with the puppy (not possible while asleep).
    Args:
        puppy (Puppy): The Puppy object being interacted with.
    Returns:
        str: A message indicating that the puppy is asleep and cannot play.
    """
    puppy.inc_plays()
    puppy.reset()
    return "The puppy is asleep. It doesn't want to play right now."
    
