import unittest


class account:
     
     def __init__(self,name,email,pin):
          account_info = {}
          self.name = name
          self.email = email
          self.pin = pin
          self.account_info = account_info
          self.account_info.update({"name":self.name})
          self.account_info.update({"email":self.email})
          self.account_info.update({"pin":self.pin})
     def __repr__(self):
          return f'\n-account name:{self.account_info.get("name")}\n-account pin:{self.account_info.get("pin")}'
     def mod_info(self,item,new):
          if item == "email":
               self.email = new
          elif item == "name":
               self.name = new
          else:
               self.pin = new
      
class balance(account):
     def __init__(self, name, email, pin,funds = 0):
          super().__init__(name, email, pin)
          self.funds= funds
     def __repr__(self):
          return f'\n-account name:{self.account_info.get("name")}\n-account balance: {self.funds}'
     def deposit(self,ammount):
          self.funds += ammount
     def withdraw(self,ammount):
          if self.funds < ammount:
               return f'sorry your can out withdraw ${ammount} from your account'
          else:
               self.funds-=ammount


# collects and processes data for the system to create base account structure
def info():
     ac = balance
     repeat = True
     while repeat:
          while True:
               print("\n-------------------------------------")
               name = input("Please enter name for account\n>>>")
               if any(char.isdigit() for char in name):
                    print("please no numbers in account name.")
                    continue
               break
          email = input("Please enter email for account\n>>>")
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
               confirm = input(f'is this correct {ac(name,email,pin)} (y/n)')
               if confirm.upper() == "N":
                    break
               elif confirm.upper() == "Y":
                    repeat != repeat
                    break
               else:
                    continue
     return ac


def funds(ac):
     while True:
          print("\n-------------------------------------")
          x = input()










