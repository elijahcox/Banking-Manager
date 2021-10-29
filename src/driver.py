from account_classes import Account, Checking, Savings, BankManager
import tkinter as tk
import time

bank_storage = BankManager()

account_gui = tk.Tk()
account_gui.title("Elijah's Banking App")
account_gui.geometry('370x412')

check_var = tk.StringVar(account_gui,"1")
save_var = tk.StringVar(account_gui,"1")
name = tk.StringVar(account_gui,"")
a = tk.StringVar(account_gui,"")
amount = tk.StringVar(account_gui,"")

def submit_account():
    check_bool = (check_var.get() == "")
    id = ""
    if check_bool:
        new_acc = Checking(name.get(),20)
        id = new_acc.ID
        bank_storage.add_account(new_acc)
    else:
        new_acc = Savings(name.get())
        id = new_acc.ID
        bank_storage.add_account(new_acc)
    new_window = tk.Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Account Number")
    L = tk.Label(new_window,text="Your Account Number is: " + id)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    L.grid(row=0,column=0)
    Q.grid(row=1,column=0)
    name.set("")
    check_var.set("1")
    save_var.set("1")

def create_account():
    new_window = tk.Toplevel(account_gui)
    new_window.title("Enter Account Details")
    new_window.geometry("250x100")
    L = tk.Label(new_window,text="Enter Name")
    T = tk.Entry(new_window,textvariable = name)
    B=tk.Button(new_window,text = 'Create Account', command=submit_account)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    R1 = tk.Radiobutton(new_window, text = "Checking", variable = check_var)
    R2 = tk.Radiobutton(new_window, text = "Savings", variable = save_var)
    L.grid(row=0,column=0)
    T.grid(row=0,column=1)
    R1.grid(row=1,column=0)
    R2.grid(row=1,column=1)
    B.grid(row = 2, column = 1)
    Q.grid(row=3, column = 2)

def query_funds():
    id = a.get()
    ret = "Balance for " + id + " is $"
    if id[0] == "S":
        if id in bank_storage.savings_accounts:
            ret += bank_storage.savings_accounts[id].check_balance()
        else:
            ret = "ERROR: Account not found"
    else:
        if id in bank_storage.checking_accounts:
            ret += bank_storage.checking_accounts[id].check_balance()
        else:
            ret = "ERROR: Account not found"
    
    new_window = tk.Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Balance")
    L = tk.Label(new_window,text=ret)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    L.grid(row=0,column=0)
    Q.grid(row=1,column=0)
    a.set("")

def check_funds():
    new_window = tk.Toplevel(account_gui)
    new_window.title("Account Balance")
    new_window.geometry("300x75")
    B=tk.Button(new_window,text = 'Check Balance', command=query_funds)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    L = tk.Label(new_window,text="Enter Account Number")
    T = tk.Entry(new_window,textvariable = a)   
    L.grid(row=0,column=0)
    T.grid(row=0,column=1)
    B.grid(row = 1, column = 1)
    Q.grid(row=2, column = 2)

def add_funds():
    id = a.get()
    ret = "Deposited $"+amount.get()+" to " + id
    if id[0] == "S":
        if id in bank_storage.savings_accounts:
            bank_storage.savings_accounts[id].deposit(int(amount.get()))
        else:
            ret = "ERROR: Account not found"
    else:
        if id in bank_storage.checking_accounts:
            bank_storage.checking_accounts[id].deposit(int(amount.get()))
        else:
            ret = "ERROR: Account not found"
    
    new_window = tk.Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Deposit Confirmation")
    L = tk.Label(new_window,text=ret)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    L.grid(row=0,column=0)
    Q.grid(row=1,column=0)
    a.set("")
    amount.set("")

def deposit_funds():
    new_window = tk.Toplevel(account_gui)
    new_window.title("Funds Deposit")
    new_window.geometry("300x90")
    B=tk.Button(new_window,text = 'Deposit Funds', command=add_funds)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    L = tk.Label(new_window,text="Enter Account Number")
    L1 = tk.Label(new_window,text="Enter Amount")
    T = tk.Entry(new_window,textvariable = a)
    T1 = tk.Entry(new_window,textvariable = amount)
    L.grid(row=0,column=0)
    T.grid(row=0,column=1)
    L1.grid(row=1,column=0)
    T1.grid(row=1,column=1)   
    B.grid(row = 2, column = 1)
    Q.grid(row=3, column = 2)

def withdraw():
    id = a.get()
    ret = "Withdrew $"+amount.get()+" from " + id
    if id[0] == "S":
        if id in bank_storage.savings_accounts:
            acc = bank_storage.savings_accounts[id]
            if int(acc.check_balance()) < int(amount.get()):
                ret = "Withdrew $"+acc.check_balance()+" from " + id
            acc.withdraw(int(amount.get()))
        else:
            ret = "ERROR: Account not found"
    else:
        if id in bank_storage.checking_accounts:
            bank_storage.checking_accounts[id].withdraw(int(amount.get()))
        else:
            ret = "ERROR: Account not found"
    
    new_window = tk.Toplevel(account_gui)
    new_window.geometry("175x50")
    new_window.title("Deposit Confirmation")
    L = tk.Label(new_window,text=ret)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    L.grid(row=0,column=0)
    Q.grid(row=1,column=0)
    a.set("")
    amount.set("")   

def withdraw_funds():
    new_window = tk.Toplevel(account_gui)
    new_window.title("Funds Withdrawal")
    new_window.geometry("300x90")
    B=tk.Button(new_window,text = 'Withdraw Funds', command=withdraw)
    Q=tk.Button(new_window,text = 'Close', command=new_window.destroy)
    L = tk.Label(new_window,text="Enter Account Number")
    L1 = tk.Label(new_window,text="Enter Amount")
    T = tk.Entry(new_window,textvariable = a)
    T1 = tk.Entry(new_window,textvariable = amount)
    L.grid(row=0,column=0)
    T.grid(row=0,column=1)
    L1.grid(row=1,column=0)
    T1.grid(row=1,column=1)   
    B.grid(row = 2, column = 1)
    Q.grid(row=3, column = 2)

#Opens box to enter account name buttons for savings or checking. if not exist, prints success  + acc number, if name exists, print error
button1=tk.Button(account_gui, text="Create Account",width = 25, height = 13)
button1.grid(row=1,column=0)
button1['command'] = create_account

#Opens box to enter account name and number. If found, opens textbox to display balance, else error
button2=tk.Button(account_gui, text="Check Balance",width = 25, height = 13)
button2.grid(row=2,column=0)
button2['command'] = check_funds

#Opens box to enter account name and number. If found, opens textbox to input funds and displays success, else error
button3=tk.Button(account_gui, text="Deposit Funds",width = 25, height = 13) 
button3.grid(row=1,column=1)
button3['command'] = deposit_funds

#Opens box to enter account name and number. If found, opens textbox to withdraw funds and displays success, else error
#If checking and over 0: print overdraft fee
#if savings and over 0: print error
button4=tk.Button(account_gui, text="Withdraw Funds",width = 25, height = 13)
button4.grid(row=2,column=1)
button4['command'] = withdraw_funds

account_gui.mainloop()