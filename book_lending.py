from datetime import datetime
import random, time

class Book:
  on_shelf = []
  on_loan = []

  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.due_date = None

  @classmethod
  def create(cls, title, author, isbn):
    book = Book(title, author, isbn)
    cls.on_shelf.append(book)
    return book

  @classmethod
  def browse(cls):
    return random.choice(cls.on_shelf)

  def lent_out(self):
    if self in self.on_loan:
      return True
    return False
  
  def current_due_date(self):
    now = datetime.now()
    # two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds
    # future_timestamp = now.timestamp() + two_weeks
    future_timestamp = now.timestamp() # for testing overdue list
    return datetime.fromtimestamp(future_timestamp)

  def borrow(self):
    if not self.lent_out():
      self.on_loan.append(self)
      self.on_shelf.remove(self)
      self.due_date = self.current_due_date()
    else:
      return f"{self.title} is not available."
    
    return f"You've borrowed {self.title}"

  @classmethod
  def overdue_books(cls):
    overdue = []
    for book in cls.on_loan:
      if book.current_due_date() < datetime.now():
        overdue.append(book)
    
    return overdue

  def return_to_library(self):
    if self.lent_out():
      self.on_loan.remove(self)
      self.on_shelf.append(self)
      self.due_date = None
      return True
    else:
      return False


aku_no_musume = Book.create("Aku no Musume: Ki No Kuroatyuuru", "Mothy", "9784569791036")
baccano = Book.create("Baccano: The Rolling Bootlegs", "Ryohgo Narita", "9784840222785")
log_horizon = Book.create("Log Horizon; The Beginning of Another World", "Mamare Touno", "9780316383059")

print(Book.browse().title)
print(Book.browse().title)
print(len(Book.on_shelf))

print(aku_no_musume.lent_out())
print(aku_no_musume.borrow())
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(aku_no_musume.lent_out())
print(aku_no_musume.borrow())
print(aku_no_musume.due_date)


time.sleep(2)
print(len(Book.overdue_books()))

print(aku_no_musume.return_to_library())
print(aku_no_musume.lent_out())
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(len(Book.overdue_books()))