from tkinter import *
from tkinter import messagebox

wigit_index =[]
class account:
     
     def __init__(self,name,email,pin,funds = 0):
          account_info = {}
          self.name = name
          self.email = email
          self.pin = pin
          self.funds= funds
          self.account_info = account_info
          self.account_info.update({"name":self.name})
          self.account_info.update({"email":self.email})
          self.account_info.update({"pin":self.pin})
     def name_account(self):
          return f'User: {self.account_info.get("name")}, email: {self.account_info.get("email")}\n'
     def __repr__(self):
          return f'\n-account name:{self.account_info.get("name")}\n-account email:{self.account_info.get("email")}\n-account pin:{self.account_info.get("pin")}\n'
     def mod_info(self,item,new):
          if item == "email":
               self.email = new
          elif item == "name":
               self.name = new
          else:
               self.pin = new
          self.account_info.update({"name":self.name})
          self.account_info.update({"email":self.email})
          self.account_info.update({"pin":self.pin})
     

     def check(self):
          return f'\n-account name:{self.account_info.get("name")}\n-account balance: {self.funds}'
     def deposit(self,ammount):
          self.funds += ammount
     def withdraw(self,ammount):
          if self.funds < ammount:
               return f'sorry your can out withdraw ${ammount} from your account'
          else:
               self.funds-=ammount
ac = account

def forget_wigit():
     while True:
          for wigit in wigit_index:
               wigit.grid_forget()
               print(wigit)
               wigit_index.remove(wigit)
          if len(wigit_index) == 0:
               break


def info_check(frame,n,e,p):
     while True:
          if any(char.isdigit() for char in n):
               name_error= Label(frame,text="please no numbers in account name.")
               name_error.grid(row=2,column=0)
               break

          else:
               try:
                    name_error.grid_forget()
               except:
                    print()
                    
          if len(e)<=0:
               email_error =  Label(frame,text="no blank emails")
               email_error.grid(row=5,column=0)
               break
          else:
               try:
                    email_error.grid_forget()
               except:
                    print()
                    
          if any(inter.isalpha() for inter in p):
               pin_error = Label(frame,text="Please no charecters in account pin.")
               pin_error.grid(row=6,column=0)
               break

          elif len(p)< 8:
               pin_error = Label(frame,text="Pin must be at least then 8 digits long")
               pin_error.grid(row=6,column=0)
               break

          else:
               try:
                    pin_error.grid_forget()
               except:
                    print()
          confirm(frame,n,e,p)

def confirm(frame,n,e,p):
     global repeat 
     while True:
          forget_wigit()         
          confirm_text = Label(frame,text = f'is this correct {ac(n,e,p)} ').grid(row=0,column=0)
          confirm_info = messagebox.askyesno()

          if confirm_info == 1:
               repeat.set(False)
               break
          else:
               break

# collects and processes data for the system to create base account structure
def info(root,testin='',testem='',testpin = ''):
     
     name = StringVar()
     email =StringVar()
     pin = StringVar()
     global repeat 
     repeat = BooleanVar()
     repeat.set(True)
     confirm = BooleanVar()

     if testin =='' and testem == '' and testpin == '':
          while repeat:
               confirm.set(False)
               frame = LabelFrame(root,padx=10,pady=10)
               frame.grid(row=0,column=0)
               

               name_text = Label(frame,text="Please enter name for account")
               name_text.grid(row=0,column=0)
               wigit_index.append(name_text)

               name = Entry(frame,width=40)
               name.grid(row=1,column=0)
               wigit_index.append(name)

               email_text = Label(frame,text="Please enter email for account")
               email_text.grid(row=3,column=0)
               wigit_index.append(email_text)

               email = Entry(frame,width=40)
               email.grid(row=4,column=0)
               email.insert(0,"ex: ######@gmail.com")
               wigit_index.append(email)

               pin_text = Label(frame,text="Please enter pin for account(min 8)")
               pin_text.grid(row=5,column=0)
               wigit_index.append(pin_text)

               pin = Entry(frame,width=40)
               pin.grid(row=6,column=0)
               wigit_index.append(pin)

               next = Button(root,text="next",command=lambda: info_check(frame,name.get(),email.get(),pin.get()))
               next.grid(row=7,column=0)


                    

     
          return ac(name.get(),email.get(),pin.get()) 
     else:
          return ac(testin,testem,testpin)