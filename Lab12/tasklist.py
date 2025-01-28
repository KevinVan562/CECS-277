from task import Task

class Tasklist:
    def __init__(self):
      """Reads file and splis it into description, date, time"""
      with open("tasklist.txt", "r") as file:
        file_list = [line.strip().split(",") for line in file]
        self._tasklist = sorted((Task(task[0], task[1], task[2]) for task in file_list))
        
    def add_task(self, desc, date, time):
        """Adds a task to the tasklist"""
        self._tasklist.append(Task(desc, date, time))
        self._tasklist.sort()

    def get_current_task(self):
        """Gets current task"""
        if len(self._tasklist) > 0:
          return self._tasklist[0]
        else:
          return None

    def mark_complete(self):
        """Marks current task as complete"""
        if len(self._tasklist) == 0:
          raise ValueError("No tasks in the list.")
        return self._tasklist.pop(0)

    def save_file(self):
        """Save the tasklist to the file"""
        with open('tasklist.txt', 'w') as file:
          file.write("\n".join([repr(task) for task in self._tasklist]))

    def __len__(self):
        """Returns the number of tasks in the tasklist"""
        return len(self._tasklist)

    def __iter__(self):
        """Iterates through the tasklist"""
        self._n = 0
        return self
      
    def __next__(self):
      """Returns the next task in the tasklist"""
      self._n += 1
      if self._n >= len(self._tasklist):
        raise StopIteration
      else:
        return self._tasklist[self._n-1]

