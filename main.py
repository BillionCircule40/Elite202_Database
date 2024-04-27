from modules import accounts
from tkinter import *
import tkinter.ttk  as tkk
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
root.geometry("500x600")
ac = accounts
ac_index = []
ac_index.append(ac.info(root,"testinfo","ian","12345678"))

def main():

     program_state = BooleanVar()
     account_login_location= IntVar()
     login_state = BooleanVar()
     choice = IntVar()
     choice.set(2)

     check_login= BooleanVar()
     while True:
          login_state.set(False)
          nextc = BooleanVar()
          nextc.set(False)
          login_state.set(False)

          quit = Button(root,text= "Exit",command=lambda:root.destroy()).grid(row=10,column=0)
          blank1 = Label(root,text="").grid(row=3,column=10)
          blank2 = Label(root,text="").grid(row=4,column=10)
          blank3 = Label(root,text="").grid(row=5,column=10)
          blank4 = Label(root,text="").grid(row=6,column=10)
          blank5 = Label(root,text="").grid(row=7,column=10)
          blank6 = Label(root,text="").grid(row=8,column=10)
          blank7 = Label(root,text="").grid(row=9,column=10)
          if login_state.get() == False:
               print("check1")
               prompt= Label(root, text="welcome to the online bank system\n-please log or create account to continue " )
               prompt.grid(row=0,column=0,columnspan=3,sticky=W+E)

               login_button = Button(root,text="login",command=lambda: choice.set(1))
               login_button.grid(row=1,column=0,padx=20)

               create_button = Button(root,text="Create account",padx=20,command= lambda:choice.set(0))
               create_button.grid(row=1,column=1)

               test = Button(root,text="test", command=lambda: print(choice.get())).grid(row=1,column=2)
               c = choice.get()
               if c == 0:
                    print("check2")
                    login_button.grid_forget()
                    create_button.grid_forget()
                    prompt.grid_forget()

                    frame = LabelFrame(root,padx=10,pady=10)
                    frame.grid(row=0,column=0,columnspan=5)
                    prompt = Label(frame,text ="Please enter account name or email")
                    prompt.grid(row=0,column=0)

                    name = Entry(frame, width=40)
                    name.grid(row=1,column=0)
                    name.insert(0,"ex: ######@gmail.com")

                    blank = Label(frame,text="")
                    blank.grid(row=2,column=0)

                    pin_text = Label(frame,text="please enter account pin")
                    pin_text.grid(row=3,column=0)

                    pin = Entry(frame,width=40)
                    pin.grid(row=4,column=0)

                    if len(pin.get())  >=8 and len(name.get())>0 :
                         next["state"] = NORMAL
                    next = Button(root,text="next",state=DISABLED)
                    next.grid(row=2,column=0)

                    if nextc.get():
                         for x in range(len(ac_index)):
                              if ac_index[x].account_info.get("name") == name or ac_index[x].account_info.get("email")== name:
                                   if ac_index[x].account_info.get("pin") == pin:
                                        account_login_location = x
                                        login_state = True
                                        break

                    if login_state.get() == False:
                         print("Invalid login\n")
               
               elif choice.get ==1:
                    ac_index.append(ac.info(root))
                    print("account created, please log to access your account")
                         
          elif login_state.get():
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
                         break
                    else: 
                         print("invaid input")
          else:
               print("fatil error")               
          root.mainloop()
     
main()