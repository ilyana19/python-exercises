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
    print("Enter First Name: ", end = '')
    first_name = input()
    print("Enter Last Name: ", end = '')
    last_name = input()
    print("Enter Email Address: ", end = '')
    email = input()
    print("Enter Note: ", end = '')
    note = input()

    Contact.create(first_name, last_name, email, note)
  
  def modify_existing_contact(self):
    return
  
  # def delete_contact(self):
  #
  #
  # def display_all_contacts(self):
  #
  # def search_by_attribute(self):

crm_app = CRM()
crm_app.main_menu()