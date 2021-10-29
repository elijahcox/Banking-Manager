class BankManager:
    user_accounts = {}
    def add_account(self,acc):
        self.user_accounts[acc.ID] = acc

class Account: #Abstract account class
    num_accounts = 0
    def __init__(self,name,account_type):
        self.ID = account_type+str(self.num_accounts)
        self.balance = 0
        self.name = name
        self.num_accounts+=1
   
    def deposit(self,amount): #encapsulation to protect balance with getter/setter
        self.balance += amount
    
    def withdraw(self,amount):#encapsulation to protect balance with getter/setter
        if self.balance - amount >= 0:
            self.balance -= amount

    def check_balance(self):#encapsulation to protect balance with getter/setter
        return self.balance

class Checking(Account): #property of inheritance: checking derives properties from Account
    def __init__(self,name,overdraft_fee:int):
        super().__init__(name,"C")
        self.overdraft_fee = overdraft_fee
    def withdraw(self,amount): #property of polymorphism: overriding inherited functions to meet child class needs
        self.balance -= amount
        if self.balance < 0:
            self.balance -= self.overdraft_fee


class Savings(Account): #property of inheritance: checking derives properties from Account
    def __init__(self,name):
        super().__init__(name,"S")
    