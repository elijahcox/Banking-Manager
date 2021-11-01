from account_classes import Account, Checking, Savings, BankManager
from tkinter import *
import time

bank_storage = BankManager()
account_gui = Tk()
account_gui.title("Elijah's Banking App")
account_gui.geometry('370x412')

check_var = StringVar(account_gui,"1")
save_var = StringVar(account_gui,"1")
name_var = StringVar(account_gui,"")
acc_num_var = StringVar(account_gui,"")
amount = StringVar(account_gui,"")

def submit_account():
    check_bool = (check_var.get() == "")
    id = bank_storage.create_account(name_var.get(),check_bool)
    new_window = Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Account Number")
    Label(new_window,text="Your Account Number is: " + id).grid(row=0,column=0)
    Button(new_window,text = 'Close', command=new_window.destroy).grid(row=1,column=0)
    name_var.set("")
    check_var.set("1")
    save_var.set("1")

def create_account():
    new_window = Toplevel(account_gui)
    new_window.title("Enter Account Details")
    new_window.geometry("250x100")
    Label(new_window,text="Enter Name").grid(row=0,column=0)
    Entry(new_window,textvariable = name_var).grid(row=0,column=1)
    Button(new_window,text = 'Create Account', command=submit_account).grid(row = 2, column = 1)
    Button(new_window,text = 'Close', command=new_window.destroy).grid(row=3, column = 2)
    Radiobutton(new_window, text = "Checking", variable = check_var).grid(row=1,column=0)
    Radiobutton(new_window, text = "Savings", variable = save_var).grid(row=1,column=1)

def query_funds():
    id = acc_num_var.get()
    ret = "Balance for " + id + " is $"
    acc = bank_storage.get_account_by_num(id)
    if  acc != -1:
        ret += acc.get_balance()
    else:
        ret = "ERROR: Account not found"
    new_window = Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Balance")
    Label(new_window,text=ret).grid(row=0,column=0)
    Button(new_window,text = 'Close', command=new_window.destroy).grid(row=1,column=0)
    acc_num_var.set("")

def check_funds():
    new_window = Toplevel(account_gui)
    new_window.title("Account Balance")
    new_window.geometry("300x75")
    Button(new_window,text = 'Check Balance', command=query_funds).grid(row = 1, column = 1)
    Button(new_window,text = 'Close', command=new_window.destroy).grid(row=2, column = 2)
    Label(new_window,text="Enter Account Number").grid(row=0,column=0)
    Entry(new_window,textvariable = acc_num_var).grid(row=0,column=1)

def add_funds():
    id = acc_num_var.get()
    ret = "Deposited $"+amount.get()+" to " + id
    acc = bank_storage.get_account_by_num(id)    
    if  acc != -1:
        acc.deposit(int(amount.get()))
    else:
        ret = "ERROR: Account not found"
    new_window = Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Deposit Confirmation")
    L = Label(new_window,text=ret).grid(row=0,column=0)
    Q=Button(new_window,text = 'Close', command=new_window.destroy).grid(row=1,column=0)
    acc_num_var.set("")
    amount.set("")

def deposit_funds():
    new_window = Toplevel(account_gui)
    new_window.title("Funds Deposit")
    new_window.geometry("300x90")
    Button(new_window,text = 'Deposit Funds', command=add_funds).grid(row = 2, column = 1)
    Button(new_window,text = 'Close', command=new_window.destroy).grid(row=3, column = 2)
    Label(new_window,text="Enter Account Number").grid(row=0,column=0)
    Label(new_window,text="Enter Amount").grid(row=1,column=0)
    Entry(new_window,textvariable = acc_num_var).grid(row=0,column=1)
    Entry(new_window,textvariable = amount).grid(row=1,column=1)   

def withdraw():
    id = acc_num_var.get()
    ret = "Withdrew $"+amount.get()+" from " + id
    acc = bank_storage.get_account_by_num(id)    
    if  acc != -1:
        acc.withdraw(int(amount.get()))
    else:
        ret = "ERROR: Account not found"
    
    new_window = Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Deposit Confirmation")
    Label(new_window,text=ret).grid(row=0,column=0)
    Button(new_window,text = 'Close', command=new_window.destroy).grid(row=1,column=0)
    acc_num_var.set("")
    amount.set("")   

def withdraw_funds():
    new_window = Toplevel(account_gui)
    new_window.title("Funds Withdrawal")
    new_window.geometry("300x90")
    Button(new_window,text = 'Withdraw Funds', command=withdraw).grid(row = 2, column = 1)
    Button(new_window,text = 'Close', command=new_window.destroy).grid(row=3, column = 2)
    Label(new_window,text="Enter Account Number").grid(row=0,column=0)
    Label(new_window,text="Enter Amount").grid(row=1,column=0)
    Entry(new_window,textvariable = acc_num_var).grid(row=0,column=1)
    Entry(new_window,textvariable = amount).grid(row=1,column=1)   

button1=Button(account_gui, text="Create Account",width = 25, height = 13)
button1.grid(row=1,column=0)
button1['command'] = create_account

button2=Button(account_gui, text="Check Balance",width = 25, height = 13)
button2.grid(row=2,column=0)
button2['command'] = check_funds

button3=Button(account_gui, text="Deposit Funds",width = 25, height = 13)
button3.grid(row=1,column=1)
button3['command'] = deposit_funds

button4=Button(account_gui, text="Withdraw Funds",width = 25, height = 13)
button4.grid(row=2,column=1)
button4['command'] = withdraw_funds

account_gui.mainloop()