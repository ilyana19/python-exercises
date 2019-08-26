emotions = {
  "happiness": 3,
  "stress": 2,
  "fear": 1,
}

# print(emotions)

class Person:
  def __init__(self, name, emotions):
    self.name = name
    self.emotions = emotions

  def __str__(self):
    return f"My name is {self.name} and I'm feeling {self.emotions}."

  def status(self):
    for emotion, value in self.emotions.items():
      if value == 1:
        print(f"I'm feeling a low amount of {emotion}.")
      elif value == 2:
        print(f"I'm feeling a medium amount of {emotion}.")
      elif value == 3:
        print(f"I am feeling a high amount of {emotion}.")


person = Person("Linda", emotions)
print(person)
person.status()