import random
import maze

class Minotaur:
    def __init__(self):
        """Initializes the minotaur's starting location and marks it"""
        maze_data = maze.Maze()._maze
        maze_rows = len(maze_data)
        maze_cols = len(maze_data[0])

        while True:
            random_row = random.randint(0, maze_rows - 1)
            random_col = random.randint(0, maze_cols - 1)
            if maze_data[random_row][random_col] == ' ':
                maze_data[random_row][random_col] = 'M'
                break

    def move_minotaur(self):
        """Moves the minotaur toward the direction of the hero"""
        maze_data = maze.Maze()._maze
        maze_rows = len(maze_data)
        maze_cols = len(maze_data[0])

        minotaur_row, minotaur_col = 0, 0
        hero_row, hero_col = 0, 0

        # Find Minotaur and Hero positions
        for i in range(maze_rows):
            for j in range(maze_cols):
                if maze_data[i][j] == 'M':
                    minotaur_row, minotaur_col = i, j
                elif maze_data[i][j] == 'H':
                    hero_row, hero_col = i, j

        # Calculate possible directions
        directions = []
        if minotaur_row < hero_row:
            directions.append('D')
        elif minotaur_row > hero_row:
            directions.append('U')
        if minotaur_col < hero_col:
            directions.append('R')
        elif minotaur_col > hero_col:
            directions.append('L')

        random.shuffle(directions)

        # Move Minotaur
        for direction in directions:
            new_row, new_col = minotaur_row, minotaur_col
            if direction == 'U':
                new_row -= 1
            elif direction == 'D':
                new_row += 1
            elif direction == 'L':
                new_col -= 1
            elif direction == 'R':
                new_col += 1

            if 0 <= new_row < maze_rows and 0 <= new_col < maze_cols and maze_data[new_row][new_col] not in ['*', 'H', 'F', 'M']:
                prev_cell = maze_data[minotaur_row][minotaur_col]
                maze_data[minotaur_row][minotaur_col] = ' '
                maze_data[new_row][new_col] = 'M'
                return prev_cell
        return None

