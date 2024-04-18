import unittest
from tkinter import *
root = Tk()


class account:
     
     def __init__(self,name,email,pin,funds = 0):
          account_info = {}
          self.name = name
          self.email = email
          self.pin = pin
          self.funds= funds
          self.account_info = account_info
          self.account_info.update({"name":self.name})
          self.account_info.update({"email":self.email})
          self.account_info.update({"pin":self.pin})
     def name_account(self):
          return f'User: {self.account_info.get("name")}, email: {self.account_info.get("email")}\n'
     def __repr__(self):
          return f'\n-account name:{self.account_info.get("name")}\n-account email:{self.account_info.get("email")}\n-account pin:{self.account_info.get("pin")}\n'
     def mod_info(self,item,new):
          if item == "email":
               self.email = new
          elif item == "name":
               self.name = new
          else:
               self.pin = new
          self.account_info.update({"name":self.name})
          self.account_info.update({"email":self.email})
          self.account_info.update({"pin":self.pin})
     

     def check(self):
          return f'\n-account name:{self.account_info.get("name")}\n-account balance: {self.funds}'
     def deposit(self,ammount):
          self.funds += ammount
     def withdraw(self,ammount):
          if self.funds < ammount:
               return f'sorry your can out withdraw ${ammount} from your account'
          else:
               self.funds-=ammount





# collects and processes data for the system to create base account structure
def info(testin='',testem='',testpin = ''):
     ac = account
     confirm_info = bool
     repeat = True
     if testin =='' and testem == '' and testpin == '':
          while repeat:
               while True:
                    print("\n-------------------------------------")
                    name = input("Please enter name for account\n>>>")
                    if any(char.isdigit() for char in name)or name == "":
                         print("please no numbers in account name.")
                         continue
                    break
               while True:
                    email = input("Please enter email for account\n>>>")
                    if email != "":
                         break
                    print("no blank emails")
               while True:
                    pin = input("Please enter pin for account(min 8)\n>>>")
                    if any(inter.isalpha() for inter in pin):
                         print("Please no charecters in account pin.")
                         continue
                    if len(pin)< 8:
                         print("Pin must be at least then 8 digits long")
                         continue
                    break
               while True:
                    
                    confirm = Label(root,text = f'is this correct {ac(name,email,pin)} \n(y/n) ')
                    button_yes = Button(root,text= "YES", fg="white",bg="green",command =lambda: confirm_info=True).grid(row=10,column=0)
                    button_no = Button(root,text= "NO", fg="white",bg="black", command = confirm_info=False).Grid(row= 10,col=1)
                    if confirm_info:
                         repeat = False
                         break
                    elif confirm_info == False:
                         break
          return ac(name,email,pin)
     else:
          return ac(testin,testem,testpin)









