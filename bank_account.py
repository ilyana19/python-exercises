class BankAccount:
  def __init__(self, balance, interest_rate):
    self.balance = balance
    self.interest_rate = interest_rate

  def __str__(self):
    return f"Balance: ${self.balance:.2f} \nInterest Rate: {self.interest_rate:.2f}%\n"

  def deposit(self, num):
    self.balance += num
    return self.balance

  def withdraw(self, num): 
    self.balance -= num
    return self.balance

  def gain_interest(self):
    self.balance += self.balance * (self.interest_rate/100)
    return self.balance

myAccount = BankAccount(1000, 1310)
print(myAccount)
myAccount.deposit(100.50)
print(myAccount)
myAccount.withdraw(0.50)
print(myAccount)
myAccount.gain_interest()
print(myAccount)