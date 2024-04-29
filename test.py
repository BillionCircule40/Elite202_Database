from tkinter import *

b = False
def click():
     global b 
     print(b)
     b= True
     

main = Tk()
main.geometry("300x100")
check = Button(main,text="press",command=click).pack()
test = Button(main,text="test",command=lambda:print(b)).pack()
if b:
     print("work")
main.mainloop()