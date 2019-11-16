print("Welcome to PiggyBank")

def deposit(amount):
  global balance
  global lt
  balance = balance + amount
  lt = amount

balance = 0
print("Balance =",balance)

lt = 0
print("Last Transaction =",balance)


deposit(50)
deposit(100)

print("Balance =",balance)
print("Last Transaction =",lt)