from modules import accounts
import tkinter
ac = accounts

ac_index = []

def main():
     program_state = True
     while program_state:
          account_login_info= ''
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
                    if (x.account.account_info.get("name")==name or x.account.account_info.get("email"))and x.account.account_info.get("pin") == pin:
                         account_login_info = x
                         login == False
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
               while login:
                    #short hand: check, dep, with, mod, del, x to simplify in terminal
                    print("\n-------------------------------------")
                    op = input(f"Welcome {account_login_info} to the online banking system, please enter what can we help you with\n-Check balance\n-Deposit\n-Withdraw\n-Modify\n-delete\n\log off\n>>>")
                    if op =="check":
                         print(account_login_info)
                    elif op == "dep":
                         amount = int(input("How much do you want to deposit?\n>>>"))
                         account_login_info.deposit(amount)
                    elif op == "with":
                         amount = int(input("How much do you want to withdraw?\n>>>"))
                         account_login_info.withdraw(amount)
                    elif op == "mod":
                         object = input("")
                         new = input("")
                         account_login_info.mod_info(object,new)
                    elif op == "del":
                         confirm = input(f"Are you sure you want to delete {account_login_info} account, (y/n)\n>>>")
                         if confirm.upper() =="Y":
                              ac_index.remove(account_login_info)
                              print("account removed")
                              login = False

                    elif op == "x":
                         print(f"thank you again {account_login_info} for using our services")
                         program_state = False
                         break
                    else: 
                         print("invaid input")


main()