# Name: Kevin Van & Isai Beltran 
# Date: 4/10/2024
# Description: A maze in which the Hero has to make it out while a Minotaur chases them.
import maze
import hero
import minotaur

def main():
    h = hero.Hero()
    mino = minotaur.Minotaur()
    m = maze.Maze()
    action = ''
    while True:
        print(m)
        while True:
            moves = ['W', 'A', 'S', 'D']
            move = input("Choose a direction (WASD): ").upper()
            if move in moves:
                break

        if move == 'W':
            action = h.go_up()
        elif move == 'S':
            action = h.go_down()
        elif move == 'A':
            action = h.go_left()
        elif move == 'D':
            action = h.go_right()

        if action == '*':
            print('You ran into a wall!')
        elif action == 'M':
            print(m)
            print('You ran into the Minotaur! Game Over!')
            break
        elif action == 'f':
            print(m)
            print("You found the exit! You win!")
            break

        mino_move = mino.move_minotaur()
        if mino_move == 'H':
            print(m)
            print('You ran into the Minotaur! Game Over!')
            break

if __name__ == "__main__":
    main()
