from random import seed
from random import randint
from datetime import date
seed(1)

class BankManager:
    checking_accounts = {}
    savings_accounts = {}
    def add_account(self,acc): #abstraction
        if acc.ID[0] == 'C':
            self.checking_accounts[acc.ID] = acc
        else:
            self.savings_accounts[acc.ID] = acc
    
    def get_account_by_num(self,num):
        if num[0] == 'C':
            if num in self.checking_accounts:
                return self.checking_accounts[num]
        elif num[0] == 'S':
            if num in self.savings_accounts:
                return self.savings_accounts[num]        

class Account: #Abstract account class
    def __init__(self,name,account_type):
        self.ID = account_type+str(randint(10,99))
        self.balance = 0
        self.name = name
        self.created_date = date.today().strftime("%d/%m/%Y")

    def deposit(self,amount): #encapsulation to protect balance with getter/setter
        self.balance += amount
    
    def withdraw(self,amount):#encapsulation to protect balance with getter/setter
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            self.balance = 0

    def check_balance(self):#encapsulation to protect balance with getter/setter
        return str(self.balance)

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
    