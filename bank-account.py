class BankAccount:
  def __init__(self, balance, interest):
    self.balance = balance
    self.interest_rate = interest

my_account = BankAccount(5000, 0.03)

print(my_account.balance)
print(my_account.interest_rate)