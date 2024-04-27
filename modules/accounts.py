from tkinter import *



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
def info(root,testin='',testem='',testpin = ''):
     ac = account
     name = StringVar()
     email =StringVar()
     pin = StringVar()
     confirm_info = BooleanVar()
     repeat = BooleanVar()
     repeat.set(True)
     if testin =='' and testem == '' and testpin == '':
          while repeat:
               
               print("\n-------------------------------------")
               acount_name = Label(root,text="Please enter name for account",)
               if any(char.isdigit() for char in name)or name == "":
                    print("please no numbers in account name.")
                    continue
               
               
               email = input("Please enter email for account\n>>>")
               
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
                    button_yes = Button(root,text= "YES", fg="white",bg="green",command =lambda: click(confirm_info,True)).grid(row=10,column=0)
                    button_no = Button(root,text= "NO", fg="white",bg="black", command =lambda: click(confirm_info,False)).Grid(row= 10,col=1)
                    if confirm_info:
                         repeat = False
                         break
                    elif confirm_info == False:
                         break
     
          root.mainloop() 
          return ac(name,email,pin)
     else:
          return ac(testin,testem,testpin)