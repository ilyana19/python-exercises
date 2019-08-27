from task import *

class TodoList:
  def __init__(self):
    self.item_list = []

  def add_task(self, item):
    self.item_list.append(item)

my_list = TodoList()
my_list.add_task(task1)
my_list.add_task(task2)
my_list.add_task(task3)

print(my_list.item_list)