# Name: Kevin Van & Isai Beltran
# Date: 4/29/24
# Description: 
import tasklist
import task
import check_input

def main_menu(): 
  """Displays the main menu and returns the user's valid input."""
  print("1. Display current task \n2. Display all tasks \n3. Mark current task complete \n4. Add new task \n5. Search by date \n6. Save and quit")
  return check_input.get_int_range("Enter a choice: ", 1, 6)

def get_date():
  """Prompts the user to enter a date in the format MM/DD/YYYY."""
  month = str(check_input.get_int_range("Enter Month: ", 1, 12))
  day = str(check_input.get_int_range("Enter Day: ", 1, 31))
  year = str(check_input.get_int_range("Enter Year: ", 2000, 2100))
  if len(month) == 1:
    month = "0" + month
  if len(day) == 1:
    day = "0" + day
  return month + "/" + day + "/" + year

def get_time():
  """Prompts the user to enter a time in the format HH:MM."""
  hour = str(check_input.get_int_range("Enter Hour: ", 0, 23))
  minute = str(check_input.get_int_range("Enter Minute: ", 0, 59))
  if len(hour) == 1:
    hour = "0" + hour
  if len(minute) == 1:
    minute = "0" + minute
  return hour + ":" + minute

def main():
  loop = True
  task_list = tasklist.Tasklist()
  while loop:
    print(f"-Tasklist- \nTasks to complete: {len(task_list)}")
    choice = main_menu()
    if choice == 1:
      print(f"Current task is: \n{task_list.get_current_task()}")
    elif choice == 2: 
      print("Tasks: ")
      [print(f"{i+1}. {task}") for i, task in enumerate(task_list)]
    elif choice == 3:
      print(f"Marking current task complete: \n{task_list.mark_complete()}")
      print(f"New current task is: \n{task_list.get_current_task()}")
    elif choice == 4:
      task_list.add_task(input("Enter a task: "), get_date(), get_time())
    elif choice == 5:
      print("Enter date to search: ")
      search_date = get_date()
      print(f"Tasks due on {search_date}:")
      tasks = [t for t in task_list if t.date == search_date]
      if not tasks:
        print(f"No tasks found for {search_date}")
      else:
        [print(f"{i+1}. {task}") for i, task in enumerate(tasks)]
    elif choice == 6:
      print("Saving and quitting...")
      task_list.save_file()
      loop = False

main()



