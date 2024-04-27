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
wigit_index =[]
ac_index = []
ac_index.append(ac.info(root,"testinfo","ian","12345678"))

def forget_wigit():
     while True:
          for wigit in wigit_index:
               wigit.grid_forget()
               print(wigit)
               wigit_index.remove(wigit)
          if len(wigit_index) == 0:
               break

def create():
     forget_wigit()
     ac_index.append(ac.info(root))
     account_create_text = Label(root,text="account created, please log to access your account")
     account_create_text.grid(row=0,column=0)


def login_check(frame,name,pin):
     global login_state
     print("check3")
     print(pin)
     print(type(pin))
     print(len(pin)>=8)
     if len(pin)<8:
          error = Label(frame,text="-pin length must be at least 8 long",fg="red")
          error.grid(row=8,column=0)
     elif len(name)<0 :
          error = Label(frame,text="-must have login email or name",fg="red")
          error.grid(row=4,column=0)

     else:
          try:
               error.grid_forget()
          except:
               print("no error")
          for x in range(len(ac_index)):
               if (ac_index[x].account_info.get("name") == name or ac_index[x].account_info.get("email")== name) and ac_index[x].account_info.get("pin") == pin:
                    print("found")
                    global account_login_location
                    account_login_location= x
                    login_state=True
                    break

          if login_state == False:
               failed_login_text=Label(frame,text="Invalid login")
               failed_login_text.grid(row=0,column= 0)
def login():
     global login_state
     while True:
          print("check2")
          forget_wigit()
                    
          frame = LabelFrame(root,padx=10,pady=10)
          frame.grid(row=0,column=0,columnspan=10)

          name_text = Label(frame,text ="Please enter account name or email")
          name_text.grid(row=0,column=0,columnspan=3)

          name = Entry(frame, width=40)
          name.grid(row=2,column=0,columnspan=3)
          name.insert(0,"ex: ######@gmail.com")

          pin_text = Label(frame,text="please enter account pin")
          pin_text.grid(row=5,column=0,columnspan=3)

          pin = Entry(frame,width=40)
          pin.grid(row=7,column=0,columnspan=3)
          
          next = Button(frame,text="next",command=lambda:login_check(frame,str(name.get()),str(pin.get())))
          next.grid(row=8,column=0)
          if login_state == True:
               break

                    
program_state = BooleanVar()
account_login_location = int

def main():


     global login_state 
     check_login= BooleanVar()
     while True:
          login_state=False
          nextc = BooleanVar()
          nextc.set(False)
          
          quit = Button(root,text= "Exit",command=lambda:root.destroy()).grid(row=10,column=0)
          blank1 = Label(root,text="").grid(row=3,column=10)
          blank2 = Label(root,text="").grid(row=4,column=10)
          blank3 = Label(root,text="").grid(row=5,column=10)
          blank4 = Label(root,text="").grid(row=6,column=10)
          blank5 = Label(root,text="").grid(row=7,column=10)
          blank6 = Label(root,text="").grid(row=8,column=10)
          blank7 = Label(root,text="").grid(row=9,column=10)
          if login_state == False:
               print("check1")
               prompt= Label(root, text="welcome to the online bank system\n-please log or create account to continue " )
               prompt.grid(row=1,column=0,columnspan=4,sticky=W+E)
               wigit_index.append(prompt)

               login_button = Button(root,text="login",command= login,padx=20)
               login_button.grid(row=2,column=0)
               wigit_index.append(login_button)

               create_button = Button(root,text="Create account",padx=20,command= create)
               create_button.grid(row=2,column=1)
               wigit_index.append(create_button)
                         
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