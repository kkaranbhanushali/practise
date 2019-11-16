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
  global balance
  global lt
  print("Balance =",balance)
  print("Last Transaction =",lt)


amount = int(input("Please enter the value to be Deposited"))

deposit(amount)
statement()

amount = int(input("Please enter the value to be Deposited"))
deposit(amount)
statement()

amount = int(input("Please enter the value to be Withdrawn"))
withdraw(amount)
statement()