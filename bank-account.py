class BankAccount:
  def __init__(self, balance, interest):
    self.balance = balance
    self.interest_rate = interest

  def __str__(self):
    return "Balance: ${:.2f} \nInterest Rate: {}%".format(self.balance, self.interest_rate * 100)

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

  def gain_interest(self):
    self.balance *= self.interest_rate +1

my_account = BankAccount(5000, 0.03)

print('--------------------------------')
print('MY ACCOUNT')
print('--------------------------------')
print(my_account)

print('--------------------------------')
print('DEPOSIT 1500')
print('--------------------------------')
my_account.deposit(1500)
print(my_account)

print('--------------------------------')
print(' WITHDRAW 150')
print('--------------------------------')
my_account.withdraw(150)
print(my_account)

print('--------------------------------')
print('GAIN INTEREST')
print('--------------------------------')
my_account.gain_interest()
print(my_account)
