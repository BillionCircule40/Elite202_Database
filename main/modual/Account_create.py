class account:
     account_info = {}
     def __init__(self,name,pin):
          self.name = name
          self.pin = pin
          account_info.update({"name":self.name})
          account_info.update({"pin":self.pin})
     def __repr__(self):
          return f'account name:{account_info.get("name")}\naccount pin:{account_info.get("pin")}' 
     

