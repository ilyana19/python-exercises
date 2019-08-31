from contact import Contact

class CRM:

  def main_menu(self):
    while True:
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)

  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print("")
    print('Enter a number: ', end = '')

  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit()

  def add_new_contact(self):
    print('\n-----------------------')
    print("Add New Contact")
    print('-----------------------')

    print("Enter First Name: ", end = '')
    first_name = input()
    print("Enter Last Name: ", end = '')
    last_name = input()
    print("Enter Email Address: ", end = '')
    email = input()
    print("Enter Note: ", end = '')
    note = input()

    Contact.create(first_name, last_name, email, note)
    print("\n")
  
  @classmethod
  def modify_existing_contact(self):
    print('\n-----------------------')
    print("Modify Contact")
    print('-----------------------')

    print("Enter the ID of the contact to edit: ", end = '')
    id = int(input())
    contact = Contact.find(id)
    attribute = input("Enter the attribute to edit: ")
    value = input("Enter the new value: ")
    print('\n-----------------------')
    setattr(contact, attribute, value)
    return contact.update
  
  def delete_contact(self):
    print('\n-----------------------')
    print("Delete Contact")
    print('-----------------------')
    print("Enter the ID to delete: ", end = '')
    contact_id = int(input())
    Contact.find(contact_id).delete()
    print('\n-----------------------')
  
  def display_all_contacts(self):
    print('\n-----------------------')
    print("Display All Contact")
    print('-----------------------')
    print(Contact.all())
    print('\n-----------------------')
  
  def search_by_attribute(self):
    print('\n-----------------------')
    print("Search Contact")
    print('-----------------------')
    attribute = input("Enter the attribute to search: ")
    value = input("Enter the value: ")
    print('-----------------------')
    print(Contact.find_by(attribute, value))
    print('\n-----------------------')

crm_app = CRM()
crm_app.main_menu()