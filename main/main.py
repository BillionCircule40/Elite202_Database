from modules import accounts
ac = accounts

ac_index = []

def main():
     while True:
          login = False
          print("welcome to the xxx bank online system\n-please log or create account to continue ")
          x = int(input("0 login, 1 create "))
          if x ==0:
               name = input("please enter account name or email\n>>>")
               while True:
                    pin = input("please enter account pin\n>>")
                    if len(pin )  >=8:
                         break
                    print("pin length must be at least 8 digits\n")
               for x in ac_index:
                    if (x.account_info.get("name")==name or x.account_info.get("email"))and x.account_info.get("pin") == pin:
                         login != login
                         break
                    else:
                         print
               if login == False:
                    print("Invalid login")

          else:
               ac_index.append(ac.info())
               print("account created, please log to access your account")
               continue
          if login:
               print()



main()