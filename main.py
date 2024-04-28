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
root.configure(background='#706e6c')
ac = accounts
wigit_index = ac.wigit_index
ac_index = []
ac_index.append(ac.info(root,"testinfo","ian","12345678"))

forget_wigit = ac.forget_wigit()

#resets program to base(does not affect local index)
def log_out():
     global login_state
     global account_login_location
     account_login_location = int 
     login_state = False
     main()

#removes account
def delete(location):
     con = ac.messagebox.askquestion("Delete Account",f"Do you want to delete {ac_index[account_login_location].name_account()}")
     if con =='yes':
          ac_index.remove(ac_index[location])
          log_out()
     else:
          ac.messagebox.showinfo

def create():
     forget_wigit()
     ac_index.append(ac.info(root))
     account_create_text = Label(root,text="account created, please log to access your account")
     account_create_text.grid(row=0,column=0)


def login_check(frame,name,pin):
     global login_state
     error = Label()
     print("check3")
     print(pin)
     if len(pin)>=8:
          error.grid_forget()
     if len(name)>0:
          error.grid_forget() 

     if len(pin)<8:
          error = Label(frame,text="-pin length must be at least 8 long",fg="red")
          error.grid(row=5,column=0)
     elif len(name)<=0 :
          error = Label(frame,text="-must have login email or name",fg="red")
          error.grid(row=2,column=0)

     else:
          for x in range(len(ac_index)):
               if (ac_index[x].account_info.get("name") == name or ac_index[x].account_info.get("email")== name) and ac_index[x].account_info.get("pin") == pin:
                    print("found")
                    try:
                         wigit_index.append(error)
                         wigit_index.append(failed_login_text)
                    except:
                         pass
                    global account_login_location
                    account_login_location= x
                    login_state=True
                    print(login_state)
                    main()

          if login_state == False:
               print("not here")
               failed_login_text=Label(frame,text="Invalid login")
               failed_login_text.grid(row=7,column= 0)
     return
def login():
     global login_state
     forget_wigit()
     print("check2")
                    
     frame = LabelFrame(root,padx=10,pady=10)
     frame.grid(row=0,column=0,columnspan=10)
     wigit_index.append(frame)

     name_text = Label(frame,text ="Please enter account name or email")
     name_text.grid(row=1,column=0,columnspan=3)
     wigit_index.append(name_text)

     name = Entry(frame, width=40)
     name.grid(row=3,column=0,columnspan=3)
     name.insert(0,"ex: ######@gmail.com")
     wigit_index.append(name)

     pin_text = Label(frame,text="please enter account pin")
     pin_text.grid(row=4,column=0,columnspan=3)
     wigit_index.append(pin_text)

     pin = Entry(frame,width=40)
     pin.grid(row=6,column=0,columnspan=3)
     wigit_index.append(pin)
          
     next = Button(frame,text="next",command=lambda:login_check(frame,str(name.get()),str(pin.get())))
     next.grid(row=8,column=0)
     wigit_index.append(next)

     #end = Button(frame,text="end",command=root.destroy())
     #end.grid(row=10,column=0)
     

     

                    
account_login_location = int
login_state=False

def main():
     global login_state 
      
     forget_wigit()

     quit = Button(root,text= "Exit program",command=lambda:root.destroy()).grid(row=10,column=0)
     blank1 = Label(root,text="").grid(row=3,column=10)
     blank2 = Label(root,text="").grid(row=4,column=10)
     blank3 = Label(root,text="").grid(row=5,column=10)
     blank4 = Label(root,text="").grid(row=6,column=10)
     blank5 = Label(root,text="").grid(row=7,column=10)
     blank6 = Label(root,text="").grid(row=8,column=10)
     blank7 = Label(root,text="").grid(row=9,column=10)

     if not login_state :
          print("check1")
          print(login_state)
          prompt= Label(root, text="welcome to the online bank system\n-please log or create account to continue " )
          prompt.grid(row=1,column=0,columnspan=4,sticky=W+E)
          wigit_index.append(prompt)

          login_button = Button(root,text="login",command= login,padx=20)
          login_button.grid(row=2,column=0)
          wigit_index.append(login_button)

          create_button = Button(root,text="Create account",padx=20,command= create)
          create_button.grid(row=2,column=1)
          wigit_index.append(create_button)
                         
     elif login_state:
          change = StringVar()
          loged_in_prompt= Label(root,text=f"Welcome {ac_index[account_login_location]} to the online banking system")
          loged_in_prompt.grid(row=0,column=0,rowspan=2,columnspan=3)
          wigit_index.append(loged_in_prompt)

          #creates blank frames to fill with the information
          fram1 = LabelFrame(root,padx=20,pady=15)
          fram1.grid(row=1,column=0,columnspan=3)
          wigit_index.append(fram1)
          fram2 = LabelFrame(root,padx=20,pady=15)
          fram2.grid(row=2,column=0,columnspan=3)
          wigit_index.append(fram2)
          fram3 = LabelFrame(root,padx=20,pady=15)
          fram3.grid(row=3,column=0,columnspan=3)
          wigit_index.append(fram3)
          fram4 = LabelFrame(root,padx=20,pady=15)
          fram4.grid(row=4,column=0,columnspan=3)
          wigit_index.append(fram4)
          fram5 = LabelFrame(root,padx=20,pady=15)
          fram5.grid(row=5,column=0,columnspan=3)
          wigit_index.append(fram5)
          fram6 = LabelFrame(root,padx=20,pady=15)
          fram6.grid(row=6,column=0,columnspan=3)
          wigit_index.append(fram1)

          #short hand: check, dep, with, mod,log, del  to simplify code names
          #check account funds 
          check_b = Button(fram1,text="Check Account Balance",command=lambda:ac_index[account_login_location].check(fram1))
          check_b.grid(row=0,column=0)
          wigit_index.append(check_b)
          #add to the account

          dep_text = Label(fram2,text="How much do you want to deposit?")
          dep_text.grid(row=0,column=0,columnspan=3)
          wigit_index.append(dep_text)

          dep_amount = Entry(fram2,width=20)
          dep_amount.grid(row=2,column=0)
          wigit_index.append(dep_amount)

          dep_b = Button(fram2,text="Deposit",command=lambda: ac_index[account_login_location].deposit(fram2,int(dep_amount.get())))
          dep_b.grid(row=3,column=0)
          wigit_index.append(del_b)

          #withdraw from account
          with_text = Label(fram3,text="How much do you want to withdraw?")
          with_text.grid(row=0,column=0,columnspan=3)
          wigit_index.append(with_text)

          with_amount = Entry(fram3,width=20)
          with_amount.grid(row=2,column=0)
          wigit_index.append(with_amount)

          with_b = Button(fram3,text="withdraw",command= lambda:ac_index[account_login_location].withdraw(fram3,int(with_amount.get())))
          with_b.grid(row=3,column=0)
          wigit_index.append(with_b)

          #check account details 
          checkD_text= Label(fram4,text="Check account information")
          checkD_text.grid(row=0,column=0,columnspan=3)
          wigit_index.append(checkD_text)

          checkD_b= Button(fram4,text="select",command=lambda:ac_index[account_login_location].info_account(fram4))
          checkD_b.grid(row=3,column=3,)
          wigit_index.append(checkD_b)

          #modify account details 
          mod_text = Label(fram5,text="")
          mod_text.grid(row=0,column=0)
          wigit_index.append(mod_text)
#ac_index[account_login_location].mod_info(object,new)
          mod_name = Radiobutton(fram5)
          mod_email = Radiobutton(fram5)
          mod_pin = Radiobutton(fram5)

          mod_b = Button(fram5,text="select")
          mod_b.grid()
          wigit_index.append(mod_b)

          #delete account
          del_text = Label(fram6,text="delete account")
          del_text.grid(row=0,column=0)
          wigit_index.append(del_text)

          del_b = Button(fram6,text="delete",command=lambda:delete())
          del_b.grid(row=1,column=0)
          wigit_index.append(del_b)
          #log out/ resets the program
          log_b = Button(root,text="logout",command=log_out)
          log_b.grid(row=9,column=0,padx=10,pady=10)
          wigit_index.append(log_b)
               

                    

                    
               
     else:
          print("fatil error")               
     
main()
root.mainloop()