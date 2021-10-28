class Account: #Abstract account class
    def __init__(self,name):
        self.ID = 0
        self.balance = 0
        self.Name = name

    def deposit(self,amount): #encapsulation to protect balance with getter/setter
        self.balance += amount
    
    def withdraw(self,amount):#encapsulation to protect balance with getter/setter
        if self.balance - amount >= 0:
            self.balance -= amount

    def check_balance(self):#encapsulation to protect balance with getter/setter
        return self.balance

class Checking(Account): #property of inheritance: checking derives properties from Account
    def __init__(self,name,overdraft_fee:int):
        super().__init__(name)
        self.overdraft_fee = overdraft_fee
    def withdraw(self,amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= self.overdraft_fee


class Savings(Account): #property of inheritance: checking derives properties from Account
    def __init__(self,name,interest_rate):
        super().__init__(name)
        self.interest_rate = interest_rate