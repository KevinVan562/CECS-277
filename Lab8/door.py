import abc


class Door(abc.ABC):
    @abc.abstractmethod
    def examine_door(self):
        """Abstract method that returns a string description of the door"""
        pass

    @abc.abstractmethod
    def menu_options(self):
        """Abstract method that returns a string of the menu options that user can choose from when attempting to unlock the door"""
        pass

    @abc.abstractmethod
    def get_menu_max(self):
        """Abstract method that returns max number of options in the above menu"""
        pass

    @abc.abstractmethod
    def attempt(self, option):
        """Abstract method that passes in the user’s selection. Uses that value to update the attributes that are needed to determine if the user"""
        pass

    @abc.abstractmethod
    def is_unlocked(self):
        """Abstract method that checks to see if the door was unlocked, returns true if it is, false otherwise"""
        pass

    @abc.abstractmethod
    def clue(self):
        """Abstract method that returns the hint that is returned if the user was unsuccessful at their attempt"""
        pass

    @abc.abstractmethod
    def success(self):
        """Abstarct method that returns the congratulatory message if the user was successful"""
        pass
