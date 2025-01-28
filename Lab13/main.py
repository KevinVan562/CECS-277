# Name: Kevin Van & Isai Beltran
# Date: 5/6/2024
# Description: Using the State pattern, create a puppy simulator program that has two 
# basic functions: to feed or play with the puppy. The puppy will react differently to 
# these functions based on which state it is currently in. The puppy has three possible 
# states: asleep, eating, or playing.
import puppy
import stateasleep
import stateeat
import stateplay
import check_input

def main():
  p = puppy.Puppy()
  print("Congratulations on your new puppy!")
  play = True
  while play:
    print("What would you like to do?")
    print("1. Feed the puppy")
    print("2. Play with the puppy")
    print("3. Quit")
    choice = check_input.get_int_range("Enter Choice: ", 1, 3)
    if choice == 1:
      print(p.give_food())
    elif choice == 2:
      print(p.throw_ball())
    elif choice == 3:
      play = False

if __name__ == "__main__":
  main()

