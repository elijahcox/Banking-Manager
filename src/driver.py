from account_classes import Account, Checking, Savings
import tkinter as tk

account_gui = tk.Tk()
account_gui.title("Elijah's Banking App")
account_gui.geometry('400x400')

#Opens box to enter account name buttons for savings or checking. if not exist, prints success  + acc number, if name exists, print error
button1=tk.Button(account_gui, text="Create Account",width = 25, height = 13)
button1.grid(row=1,column=0)

#Opens box to enter account name and number. If found, opens textbox to display balance, else error
button2=tk.Button(account_gui, text="Check Balance",width = 25, height = 13)
button2.grid(row=2,column=0)

#Opens box to enter account name and number. If found, opens textbox to input funds and displays success, else error
button2=tk.Button(account_gui, text="Deposit Funds",width = 25, height = 13) 
button2.grid(row=1,column=1)

#Opens box to enter account name and number. If found, opens textbox to withdraw funds and displays success, else error
#If checking and over 0: print overdraft fee
#if savings and over 0: print error
button2=tk.Button(account_gui, text="Withdraw Funds",width = 25, height = 13)
button2.grid(row=2,column=1)


account_gui.mainloop()