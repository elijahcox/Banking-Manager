class Account: #Abstract account class
    def __init__(name):
        self.ID = 0
        self.balance = 0
        self.Name = name

    def deposit(amount): #encapsulation to protect balance with getter/setter
        self.balance += amount
    
    def withdraw(amount):#encapsulation to protect balance with getter/setter
        if balance - amount >= 0:
            self.balance -= amount

    def check_balance():#encapsulation to protect balance with getter/setter
        return self.balance

class Checking(Account): #property of inheritance: checking derives properties from Account
    def __init__(name,overdraft_fee:int):
        super().__init__(name)
        self.overdraft_fee = overdraft_fee
    def withdraw(amount):
        self.balance -= amount
        if balance < 0:
            balance -= overdraft_fee


class Savings(Account): #property of inheritance: checking derives properties from Account
    def __init__(name,interest_rate):
        super().__init__(name)
        self.interest_rate = interest_rate