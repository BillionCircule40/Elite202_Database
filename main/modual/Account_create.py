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
     

