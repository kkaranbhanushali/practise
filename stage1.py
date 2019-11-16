print("Welcome to PiggyBank")

balance = 0
print("Balance =",balance)

lt = 0
print("Last Transaction =",balance)

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


deposit(50)
deposit(100)

print("Balance =",balance)
print("Last Transaction =",lt)

withdraw(70)

print("Balance =",balance)
print("Last Transaction =",lt)