class Task:
  def __init__(self, description, due_date):
    self.description = description
    self.due_date = due_date

  def __str__(self):
    return f"Task: {self.description} ----- Due Date: {self.due_date}"

  def __repr__(self):
    return self.__str__()

task1 = Task("Create a task", "2019/08/30")
task2 = Task("Save the work", "2019/08/30")
task3 = Task("Update Git", "2019/08/30")
# print(task1)
# print(task2)
# print(task3)