class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Hi, my name is {self.name}")

class Student(Person):
  def learn(self):
    print("I get it!")

class Instructor(Person):
  def teach(self):
    print("An object is an instance of a class")


nadia = Instructor("Nadia")
nadia.greet()
chris = Student("Chris")
chris.greet()

nadia.teach()
chris.learn()