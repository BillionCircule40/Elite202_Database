class account:
     
     def __init__(self,name,pin):
          account_info = {}
          self.name= name
          self.pin= pin
          self.account_info = account_info
          self.account_info.update({"name":self.name})
          self.account_info.update({"pin":self.pin})
     def __repr__(self):
          return f'account name:{self.account_info.get("name")}\naccount pin:{self.account_info.get("pin")}' 
     
def info():
     while True:
          print("\n-------------------------------------")
          name = input("Please enter name for account\n>>>")
          if any(char.isdigit() for char in name):
               print("please no numbers in account name.")
               continue
          break
     while True:
          pin = input("Please enter pin for account\n>>>")
          if any(inter.isalpha() for inter in pin):
               print("please no charecters in account pin.")
               continue
          break












def main():
     while True:
          print("welcome to the xxx bank online system\n-please log or create account to continue ")
          x = int(input("0 login, 1 create"))
          if x ==0:
               print('log')
          else:
               print(info.info())



main()