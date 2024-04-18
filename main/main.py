from modules import accounts
from tkinter import *
root = Tk()
root.title("Online Bank system")

ac = accounts
ac_index = []

def main():
     program_state = True
     ac_index.append(ac.info("testinfo","ian","12345678"))
     
     while program_state:
          account_login_info= ''
          login_state = False
          intro_prompt= Label(root, text="welcome to the online bank system\n-please log or create account to continue " ).grid(row=0,column=0)
          login_button = Button(root,text="login",command= ).Grid(row=1,column=0)
          test = Button(root,text="" )
          create_button = Button(root,text="Create account").Grid(row=1,column=0)
          x = int(input("0 login, 1 create\n>>> "))
          if x ==0:
               name = input("please enter account name or email\n>>>")
               while True:
                    pin = input("please enter account pin\n>>")
                    if len(pin )  >=8:
                         break
                    print("pin length must be at least 8 digits\n")

               for x in range(len(ac_index)):
                    if ac_index[x].account_info.get("name") == name or ac_index[x].account_info.get("email")== name:
                         if ac_index[x].account_info.get("pin") == pin:
                              account_login_info = x
                              login_state = True
                              break

               if login_state == False:
                    print("Invalid login\n")

          else:
               ac_index.append(ac.info())
               print("account created, please log to access your account")
               continue
          if login_state:
               while login_state:
                    #short hand: check, dep, with, mod, del, x to simplify in terminal
                    print("\n-------------------------------------")
                    op = input(f"Welcome {ac_index[account_login_info]} to the online banking system, please enter what can we help you with\n-Check balance\n-Deposit\n-Withdraw\n-Modify\n-delete\n\log off\n>>>")
                    if op =="check":
                         print(ac_index[account_login_info].check())
                    elif op == "dep":
                         amount = int(input("How much do you want to deposit?\n>>>"))
                         ac_index[account_login_info].deposit(amount)
                    elif op == "with":
                         amount = int(input("How much do you want to withdraw?\n>>>"))
                         ac_index[account_login_info].withdraw(amount)
                    elif op == "mod":
                         object = input("please enter what you want to change(name,email,pin)\n>>>")
                         new = input("")
                         ac_index[account_login_info].mod_info(object,new)
                    elif op == "del":
                         confirm = input(f"Are you sure you want to delete {ac_index[account_login_info].name_account()} account, (y/n)\n>>>")
                         if confirm.upper() =="Y":
                              ac_index.remove(ac_index[account_login_info])
                              print("account removed")
                              login_state = False

                    elif op == "x":
                         print(f"thank you again {ac_index[account_login_info].name_account()} for using our services")
                         program_state = False
                         break
                    else: 
                         print("invaid input")

     root.mainloop()
main()