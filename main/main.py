#from  Account_create import account as AC

class account:
     
     def __init__(self,name,pin):
          account_info = {}
          self.name= name
          self.pin= pin
          self.account_info = account_info
          self.account_info.update({"name":self.name})
          self.account_info.update({"pin":self.pin})
     def __repr__(self):
          return f'account name: {self.account_info.get("name")}\naccount pin: {self.account_info.get("pin")}' 
     




def main():
     while True:
          print("welcome to the xxx bank online system\n-please log or create account to continue ")
          print(account("ellie","01001"))
          x = int(input("0 login, 1 create"))
          if x ==0:
               print('log')
          else:
               #AC()
               print('log1')



main()