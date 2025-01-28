import maze

class Hero:
    def __init__(self):
        """Sets the hero's starting location and marks it"""
        self.position = maze.Maze().search_maze()
        if not self.position:
            raise ValueError("Start position 's' not found in the maze.")
        else:
            maze.Maze()[self.position[0]][self.position[1]] = 'H'  # Set Hero's initial position

    def go_up(self):
        """Updates the hero's location by moving up one row if possible"""
        row, col = self.position
        new_row = row - 1
        if new_row >= 0 and maze.Maze()[new_row][col] != '*':
            prev_char = maze.Maze()[new_row][col]
            maze.Maze()[row][col] = ' '
            maze.Maze()[new_row][col] = 'H'
            self.position = (new_row, col)
            return prev_char
        else:
            return '*'

    def go_down(self):
        """Updates the hero's location by moving down one row if possible"""
        row, col = self.position
        new_row = row + 1
        if new_row < len(maze.Maze()) and maze.Maze()[new_row][col] != '*':
            prev_char = maze.Maze()[new_row][col]
            maze.Maze()[row][col] = ' '
            maze.Maze()[new_row][col] = 'H'
            self.position = (new_row, col)
            return prev_char
        else:
            return '*'

    def go_left(self):
        """Updates the hero's location by moving left one column if possible"""
        row, col = self.position
        new_col = col - 1
        if new_col >= 0 and maze.Maze()[row][new_col] != '*':
            prev_char = maze.Maze()[row][new_col]
            maze.Maze()[row][col] = ' '
            maze.Maze()[row][new_col] = 'H'
            self.position = (row, new_col)
            return prev_char
        else:
            return '*'

    def go_right(self):
        """Updates the hero's location by moving right one column if possible"""
        row, col = self.position
        new_col = col + 1
        if new_col < len(maze.Maze()[0]) and maze.Maze()[row][new_col] != '*':
            prev_char = maze.Maze()[row][new_col]
            maze.Maze()[row][col] = ' '
            maze.Maze()[row][new_col] = 'H'
            self.position = (row, new_col)
            return prev_char
        else:
            return '*'

