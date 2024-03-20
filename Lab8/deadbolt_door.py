import door
import random


class Deadbolt_door(door.Door):
    def __init__(self):
        """Randomizes the initial state of the door (either locked or unlocked)"""
        self._bolt1 = random.randint(0, 1)  # 0 for locked, 1 for unlocked
        self._bolt2 = random.randint(0, 1)

    def examine_door(self):
        """Returns a string description of the door"""
        return "You encounter a double deadbolt door, both deadbolts must be unlocked to open the door, but you can't tell if each one is locked or unlocked.\n"

    def menu_options(self):
        """Returns a string of the menu options that user can choose from when attempting to unlock the door"""
        return "1. Toggle Bolt 1\n2. Toggle Bolt 2\n"

    def get_menu_max(self):
        """Returns the number of options in the above menu"""
        return 2

    def attempt(self, option):
        """Passes in the user’s selection. Uses that value to update the attributes that are needed to determine if the door is unlocked or still locked"""
        if option == 1:
            self._bolt1 = not self._bolt1
            return "You toggle the first bolt.\n"
        elif option == 2:
            self._bolt2 = not self._bolt2
            return "You toggle the second bolt.\n"
        else:
            return "Invalid option"

    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise"""
        return self._bolt1 == 1 and self._bolt2 == 1

    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt"""
        if self._bolt1 == 0 and self._bolt2 == 0:
            return "You jiggle the door...it seems like it's completely locked.\n"
        elif self._bolt1 == 1 or self._bolt2 == 1:
            return "You jiggle the door... it seems like one of the bolts is unlocked.\n"

    def success(self):
        """Returns the congratulatory message if the user was successful"""
        return "You unlocked both deadbolts and opened the door.\n"
