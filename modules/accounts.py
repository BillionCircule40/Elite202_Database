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
     def info_account(self):
          return f'\n-account name:{self.account_info.get("name")}\n-account email:{self.account_info.get("email")}\n-account pin:{self.account_info.get("pin")}\n'
     def mod_info(self,item,new,locat):
          if item == "email":
               change = Label(locat,text="change of email successful")
               change.grid(row=5,column=0)
               wigit_index.append(change)
               self.email = new
          elif item == "name":
               change = Label(locat,text="change of name successful")
               change.grid(row=5,column=0)
               wigit_index.append(change)
               self.name = new
          elif item == "pin":
               change = Label(locat,text="change of pin successful")
               change.grid(row=5,column=0)
               wigit_index.append(change)
               self.pin = new
          
          self.account_info.update({"name":self.name})
          self.account_info.update({"email":self.email})
          self.account_info.update({"pin":self.pin})
     

     def check(self,locat):
          check = Label(locat,text=f'-account name: {self.account_info.get("name")}\n-account balance: {self.funds}')
          check.grid(row=1,column=0,columnspan=5,padx=100)
          wigit_index.append(check)
     
     def deposit(self,locat,ammount = 0):
          if not ammount<0:
               try:
                    invalid.grid_forget()
               except:
                    pass
               suc = Label(locat,text=f"successful deposit of ${ammount}")
               suc.grid(row=3,column=0)
               wigit_index.append(suc)
               self.funds += ammount
          else:
               invalid = Label(locat,text=f"you canot deposit ${ammount} to your account",fg="red")
               invalid.grid(row=1,column=0,pady=5)
               wigit_index.append(invalid)

     def withdraw(self,locat,ammount):
          if not self.funds < ammount:
               try:
                    invalid.grid_forget()
               except:
                    pass
               suc = Label(locat,text=f"successful withdraw of ${ammount}")
               suc.grid(row=3,column=0)
               wigit_index.append(suc)
               self.funds-=ammount
          else:
               invalid = Label(locat,text=f"invalid balace on withdraw  of${ammount} from your account",fg="red")
               invalid.grid(row=3,column=0,pady=5)
               wigit_index.append(invalid)
ac = account

def forget_wigit():
     while True:
          for wigit in wigit_index:
               try:
                    wigit.grid_forget()
                    print(wigit)
                    wigit_index.remove(wigit)
               except:
                    pass
          if len(wigit_index) == 0:
               break


def info_check(frame,n,e,p):
     if any(char.isdigit() for char in n) or len(n)<=0 or len(e)<=0 or any(inter.isalpha() for inter in p) or len(p)< 8:
          if any(char.isdigit() for char in n):
               name_error= Label(frame,text="please no numbers in account name.",fg="red")
               name_error.grid(row=2,column=0)
               wigit_index.append(name_error)
                              
          if len(n)<=0:
               name_error= Label(frame,text="no blank account names.",fg="red")
               name_error.grid(row=3,column=0)
               wigit_index.append(name_error)

          if len(e)<=0:
               email_error =  Label(frame,text="no blank emails",fg="red")
               email_error.grid(row=6,column=0)
               wigit_index.append(email_error)
                         
          if any(inter.isalpha() for inter in p):
               pin_error = Label(frame,text="Please no charecters in account pin.",fg="red")
               pin_error.grid(row=10,column=0)
               wigit_index.append(pin_error)
                    

          if len(p)< 8:
               pin_error = Label(frame,text="Pin must be at least then 8 digits long",fg="red")
               pin_error.grid(row=11,column=0)
               wigit_index.append(pin_error)
                    

     else:       
          confirm(n,e,p)
#prompt user to check if the inputed information is correct 
def confirm(n,e,p):
     global name 
     global email 
     global pin
     forget_wigit()         
     confirm_info = messagebox.askquestion("confirm",f"is this correct {ac(n,e,p).info_account()} ")
     if confirm_info == "yes":
          name = n
          email = e
          pin = p
     else:
          info()



name = ""
email =""
pin = ""
# collects and processes data for the system to create base account structure
def info(root,testin='',testem='',testpin = ''):
     forget_wigit()
     global name 
     global email 
     global pin 
     if not name == "" and not email == "" and not pin == ""  :
          return ac(name,email,pin)
     if testin =='' and testem == '' and testpin == '':  
          #generate fram for infromation
          frame = LabelFrame(root,padx=10,pady=10)
          frame.grid(row=0,column=0,columnspan=10,rowspan=11)
          wigit_index.append(frame)

          #generate to intro 
          ac_creat_intro_prompt = Label(frame,text="Welcome to account creation, please enter the following information to continue.")
          ac_creat_intro_prompt.grid(row=0,column=0,columnspan=3)
          wigit_index.append(ac_creat_intro_prompt)

          #generate name promt
          name_text = Label(frame,text="Please enter name for account")
          name_text.grid(row=1,column=0)
          wigit_index.append(name_text)

          #collect chosen name
          name_input = Entry(frame,width=40)
          name_input.grid(row=4,column=0)
          wigit_index.append(name_input)

          #generate email promt
          email_text = Label(frame,text="Please enter email for account")
          email_text.grid(row=5,column=0)
          wigit_index.append(email_text)

          #collect chosen email 
          email_input = Entry(frame,width=40)
          email_input.grid(row=8,column=0)
          email_input.insert(0,"ex: ######@gmail.com")
          wigit_index.append(email_input)

          #generate pin promt
          pin_text = Label(frame,text="Please enter pin for account(min 8)")
          pin_text.grid(row=9,column=0)
          wigit_index.append(pin_text)

          #collect chosen pin number
          pin_input = Entry(frame,width=40)
          pin_input.grid(row=11,column=0)
          wigit_index.append(pin_input)

          #check info and poes errors if missing or invalid information is present when clicked 
          next = Button(root,text="next",command=lambda: info_check(frame,name_input.get(),email_input.get(),pin_input.get()))
          next.grid(row=12,column=0)


                    

     
           
     else:
          return ac(testin,testem,testpin)