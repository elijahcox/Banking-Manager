from random import seed
from random import randint
from datetime import date
import sqlite3
from sqlite3 import Error
from os.path import exists
import os
seed(1)

command = """CREATE TABLE IF NOT EXISTS projects (
	id integer PRIMARY KEY,
	name text NOT NULL,
	begin_date text,
	end_date text
);"""


class BankManager:
    checking_accounts = {}
    savings_accounts = {}

    def __init__(self):
        self.load_db()
    
    def load_db(self):
        path = os.getcwd()+"\\db\\bank.db"
        db_found = exists(path)
        conn = None
        try:
            conn = sqlite3.connect(path) 
            if db_found != True:
                cursor = conn.cursor()
                cursor.execute(command)
        except Error as e:
            pass
        finally:
            if conn:
                conn.close()

    def create_account(self,name,is_check):
        if is_check == True:
            new_check = Checking(name,25)
            self.add_account(new_check)
            return new_check.ID
        else:
            new_save = Savings(name)
            self.add_account(Savings(name))
            return new_save.ID

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
        return -1

    def get_account_by_name(self,name):
        accs = []
        for k,v in self.checking_accounts.items():
            if v.get_name() == name:
                accs.append(v)
        
        for k,v in self.savings_accounts.items():
            if v.get_name() == name:
                accs.append(v)
        return accs

class Account: #Abstract account class
    def __init__(self,name,account_type):
        self.ID = account_type+str(randint(10,99))
        self.balance = 0
        self.name = name
        self.created_date = date.today().strftime("%d/%m/%Y")

    def get_name(self):
        return self.name
    
    def get_ID(self):
        return self.ID

    def get_balance(self):#encapsulation to protect balance with getter/setter
        return str(self.balance)

    def deposit(self,amount): #encapsulation to protect balance with getter/setter
        self.balance += amount
    
    def withdraw(self,amount):#encapsulation to protect balance with getter/setter
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            self.balance = 0

class Checking(Account): #property of inheritance: checking derives properties from Account
    def __init__(self,name,overdraft_fee:int):
        super().__init__(name,"C")
        self.overdraft_fee = overdraft_fee
    
    def withdraw(self,amount): #property of polymorphism: overriding inherited functions to meet child class needs
        if self.balance > 0:
            self.balance -= amount
            if self.balance < 0:
                self.balance -= self.overdraft_fee

class Savings(Account): #property of inheritance: checking derives properties from Account
    def __init__(self,name):
        super().__init__(name,"S")
    