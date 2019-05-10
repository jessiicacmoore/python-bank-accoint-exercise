class BankAccount:
  def __init__(self, balance, interest):
    self.balance = balance
    self.interest_rate = interest

  def __str__(self):
    return f"Balance: {self.balance} \nInterest Rate: {self.interest_rate * 100}%"

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

my_account = BankAccount(5000, 0.03)

print(my_account)

my_account.deposit(1500)
print(my_account)

my_account.withdraw(150)
print(my_account)