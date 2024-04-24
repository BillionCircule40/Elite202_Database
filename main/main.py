from modules import accounts
from tkinter import *
#import mysql.connector


#connection  = mysql.connector.connect(
#     user='root',
#     password='test1234',
#     database='bank_database'
#     )
#cursor = connection.cursor()
#addData = ("INSERT INTO account_info (account_name, account_email, account_pin,account_balence) VALUES (test,teste,11111111)")
#cursor.execute(addData)
#connection.commit()
#cursor.close()

root = Tk()
root.title("Online Bank system")

ac = accounts
ac_index = []


def main():
     program_state = BooleanVar()
     ac_index.append(ac.info("testinfo","ian","12345678"))
     account_login_location= IntVar()
     login_state = BooleanVar()
     choice = ""
     prompt= Label(root, text="welcome to the online bank system\n-please log or create account to continue " ).grid(row=0,column=0)
     login_button = Button(root,text="login",command= lambda: ac.click(choice=0)).Grid(row=1,column=0)
     create_button = Button(root,text="Create account",command= lambda: ac.click(choice=1)).Grid(row=1,column=0)

     root.mainloop()
     if choice ==0:
          login_button.grid_forget()
          create_button.grid_forget()
          prompt.grid_forget()
          prompt = Label(root,text ="Please enter account name or email").grid(row=0,column=0)
          name = Entry(root, width=40).grid(row=1,column=0)
          name.insert(0,"ex: ######@gmail.com")
          next = Button(root,text="next",command=ac.click(choice,True)).grid(row=2,column=0)
          if choice:
               prompt.grid_forget()
               name.grid_forget()

               pin = Entry(0,"please enter account pin\n>>")
               next = Button(root,text="next",state=DISABLED)
               if len(pin.get())  >=8:
                    next["state"] = NORMAL
                         
                    

               for x in range(len(ac_index)):
                    if ac_index[x].account_info.get("name") == name or ac_index[x].account_info.get("email")== name:
                        if ac_index[x].account_info.get("pin") == pin:
                              account_login_location = x
                              login_state = True
                              break

               if login_state == False:
                    print("Invalid login\n")
     
     else:
          ac_index.append(ac.info())
          print("account created, please log to access your account")
               
     if login_state:
          login_button.grid_forget()
          create_button.grid_forget()
          prompt.grid_forget()
          while login_state:
               #short hand: check, dep, with, mod, del, x to simplify in terminal
               print("\n-------------------------------------")
               op = input(f"Welcome {ac_index[account_login_location]} to the online banking system, please enter what can we help you with\n-Check balance\n-Deposit\n-Withdraw\n-Modify\n-delete\n\log off\n>>>")
               if op =="check":
                    print(ac_index[account_login_location].check())
               elif op == "dep":
                    amount = int(input("How much do you want to deposit?\n>>>"))
                    ac_index[account_login_location].deposit(amount)
               elif op == "with":
                    amount = int(input("How much do you want to withdraw?\n>>>"))
                    ac_index[account_login_location].withdraw(amount)
               elif op == "mod":
                    object = input("please enter what you want to change(name,email,pin)\n>>>")
                    new = input("")
                    ac_index[account_login_location].mod_info(object,new)
               elif op == "del":
                    confirm = input(f"Are you sure you want to delete {ac_index[account_login_location].name_account()} account, (y/n)\n>>>")
                    if confirm.upper() =="Y":
                         ac_index.remove(ac_index[account_login_location])
                         print("account removed")
                         login_state = False

               elif op == "x":
                    print(f"thank you again {ac_index[account_login_location].name_account()} for using our services")
                    program_state = False
                    break
               else: 
                    print("invaid input")

     
main()