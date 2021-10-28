from account_classes import Account, Checking, Savings

x = Checking('John',25)
x.deposit(15)
x.withdraw(16)
print(x.check_balance())