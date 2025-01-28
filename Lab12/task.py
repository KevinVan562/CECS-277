class Task:
  def __init__(self, desc, date, time):
    """
    Attributes:
      desc (str): description of the task
      date (str): due date of the task
      time (str): time the task is due
    """
    self._description = desc
    self._date = date
    self._time = time

  @property
  def date(self):
    return self._date
    
  def __str__(self):
    """Return a string representation of the object."""
    return  f"{self._description} - Due: {self._date} at {self._time}"

  def __repr__(self):
    """Format how task is stored in tasklist.txt"""
    return f"{self._description},{self._date},{self._time}"

  def __lt__(self, other):
    """Lists tasks in order of date, time and description"""
    self_date_parts = self._date.split("/")
    other_date_parts = other._date.split("/")

    # Compare years first
    if int(self_date_parts[2]) != int(other_date_parts[2]):
        return int(self_date_parts[2]) < int(other_date_parts[2])

    # Compare months
    if int(self_date_parts[0]) != int(other_date_parts[0]):
        return int(self_date_parts[0]) < int(other_date_parts[0])

    # Compare days
    if int(self_date_parts[1]) != int(other_date_parts[1]):
        return int(self_date_parts[1]) < int(other_date_parts[1])

    # Compare times if dates are equal
    self_time_parts = self._time.split(":")
    other_time_parts = other._time.split(":")

    if int(self_time_parts[0]) != int(other_time_parts[0]):
        return int(self_time_parts[0]) < int(other_time_parts[0])

    if int(self_time_parts[1]) != int(other_time_parts[1]):
        return int(self_time_parts[1]) < int(other_time_parts[1])

    # If dates and times are equal, compare descriptions
    return self._description < other._description
      
    
      
