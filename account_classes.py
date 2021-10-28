class Account:
    def __init__(name):
        self.ID = 0
        self.balance = 0
        self.Name = name

    def deposit(amount):
        self.balance += amount
    
    def withdraw(amount):
        self.balance -= amount

    def check_balance():
        return self.balance

class Checking(Account):
    pass

class Savings(Account):
    pass