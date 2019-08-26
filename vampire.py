class Vampire:
  coven = []

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.in_coffin = True
    self.drank_blood_today = False

  def __str__(self):
    return f"Name: {self.name}, Age: {self.age}, In Coffin? {self.in_coffin}, Drank Blood? {self.drank_blood_today}"

  def __repr__(self):
    return self.__str__()

  def drink_blood(self):
    self.drank_blood_today = True

  def go_home(self):
    self.in_coffin = True

  @classmethod
  def create(cls, name, age):
    vampire = Vampire(name, age)
    cls.coven.append(vampire)
    return vampire

  @classmethod
  def sunrise(cls):
    for self in cls.coven:
      if self.in_coffin == False or self.drank_blood_today == False:
        cls.coven.remove(self)

    return cls.coven

  @classmethod
  def sunset(cls):
    for vampire in cls.coven:
      vampire.in_coffin = False
      vampire.drank_blood_today = False
    return vampire.coven

zero = Vampire.create('Zero', 17)
yuuki = Vampire.create('Yuuki', 16)
kaname = Vampire.create('Kaname', 20)

# print(Vampire.coven)
# zero.drink_blood()
# print(Vampire.coven)
Vampire.sunset()
# print(Vampire.coven)
zero.drink_blood()
yuuki.drink_blood()
zero.go_home()
yuuki.go_home()
kaname.drink_blood()
print("******************")
print(Vampire.coven)
Vampire.sunrise()
print("---------------")
print(Vampire.coven)