class Contact:
  contacts = []
  next_id = 1

  def __init__(self, first_name, last_name, email, note):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = Contact.next_id
    Contact.next_id += 1

  def __repr__(self):
    return f"{self.id} {self.first_name} {self.last_name} {self.email} {self.note}"


  @classmethod
  def create(cls, first_name, last_name, email, note):
    new_entry = Contact(first_name, last_name, email, note)
    cls.contacts.append(new_entry)
    return new_entry

  @classmethod
  def all(cls):
    for contact in cls.contacts:
      print(contact)

  @classmethod
  def find(cls, id):
    for contact in cls.contacts:
      if id == contact.id:
        return contact

  def update(self, attribute, value):
    setattr(self, attribute, value)
    return self


  @classmethod
  def find_by(cls, attribute, value):
    for contact in cls.contacts:
      if getattr(contact, attribute) == value:
        return contact


  @classmethod
  def delete_all(cls):
    del cls.contacts[:] # supposedly faster way
    # cls.contacts.clear()
    return print("Removed all items")


  def full_name(self):
    return f"{self.first_name} {self.last_name}"


  def delete(self):
    Contact.contacts.remove(self)
    return print("Conact removed")

  # Feel free to add other methods here, if you need them.

# contact = Contact('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# print(contact)

# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
# print(len(Contact.contacts))
# print(contact1.id)
# print(contact2.id)
# print(Contact.contacts)
# print("\n")
# Contact.all()
# print("\n")

# print(Contact.find(2))
# print(Contact.find(2).full_name())
# Contact.find(2).update('note', 'beep boop beep boop')
# print("\n")
# Contact.all()
# print("\n")

# print(Contact.find_by('first_name', 'Betty'))
# print(Contact.find_by('email', 'bettymakes@bitmakerlabs.com'))
# print("\n")
# Contact.all()
# print("\n")
# Contact.find(2).delete()
# Contact.all()
# print("\n")

# print("---------------")
# Contact.delete_all()
# Contact.all()