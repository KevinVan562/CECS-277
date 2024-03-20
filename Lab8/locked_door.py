import door
import random


class Locked_door(door.Door):

    def __init__(self):
        """Randomizes the location of the key"""
        self._key_location = random.randint(1, 3)
        self._input = 0

    def examine_door(self):
        """Returns a string description of the door"""
        return "A locked door. Look around for the key.\n"

    def menu_options(self):
        """Returns a string of the menu options that user can choose from when attempting to unlock the door"""
        return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock\n"

    def get_menu_max(self):
        """Returns the number of options in the above menu"""
        return 3

    def attempt(self, option):
        """Passes in the user’s selection"""
        self._input = option
        if option == 1:
            return "You look under the mat.\n"
        elif option == 2:
            return "You look under the flower pot.\n"
        elif option == 3:
            return "You look under the fake rock.\n"
        else:
            return "Invalid option.\n"

    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise"""
        return self._key_location == self._input

    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt"""
        return "Look somewhere else.\n"

    def success(self):
        """Returns the congratulatory message if the user was successful"""
        return "Congratulations, you found the key and opened the door.\n"
