import puppystate
import stateeat
import stateasleep

class StatePlay(puppystate.PuppyState):
    def feed(self, puppy):
        """
        Attempt to feed the puppy while it is playing.
        Args:
            puppy (Puppy): The Puppy object being interacted with.
        Returns:
            str: A message indicating that the puppy is too busy playing to eat.
        """
        puppy.inc_feeds()
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        """
        Play with the puppy and potentially transition its state.
        Args:
            puppy (Puppy): The Puppy object being interacted with.
        Returns:
            str: A message indicating the result of the play action.
        """
        puppy.inc_plays()
        if puppy.plays < 3:
            return "You throw the ball again and the puppy excitedly chases it."
        else:
            puppy.change_state(stateasleep.StateAsleep())
            return "You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"

