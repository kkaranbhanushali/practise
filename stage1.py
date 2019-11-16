print("Welcome to PiggyBank")

balance = 0
lt = 0

def deposit(amount):
  global balance
  global lt
  if(amount > 0):
      balance = balance + amount
      lt = amount

def withdraw(amount):
  global balance
  global lt
  if(balance >= amount):
      balance = balance - amount
      lt = -amount

def statement():
  print("Balance =",balance)
  print("Last Transaction =",lt)


deposit(50)
statement()

deposit(100)
statement()

withdraw(70)
statement()