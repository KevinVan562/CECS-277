class Maze:
  _instance = None
  _initialized = False

  def __new__ (cls):
    """Constructs and returns the Maze"""
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__ (self):
    """Initializes the maze"""
    if (not Maze._initialized):
      file = open(f'minomaze.txt')
      self._maze = []
      for row in file:
        line = []
        for item in row:
          if (item != ''):
            line.append(item)
        self._maze.append(line)
      file.close()
      Maze._initialized = True

  def __getitem__ (self, row):
    '''Takes the index for a wanted row as an input. Outputs the contents in that row as a list'''
    return self._maze[row]

  def __len__ (self):
    '''Outputs the number of rows in the maze.'''
    return len(self._maze)

  def __str__ (self):
    '''Outputs the contents of the maze as a string.'''
    string = ''
    for row in self._maze:
      for item in row:
        string += item
    return string

  def search_maze (self):
    """Returns the location of the character in the maze as a two item 1D list"""
    start = []
    for row in self._maze:
      if ('s' not in row):
        continue
      start.append(self._maze.index(row))
      for item in row:
        if (item == 's'):
          start.append(row.index(item))
    return start

