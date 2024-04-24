import tkinter 
import os
if os.environ.get('DISPLAY','') == '':
     print('no display')
     os.environ.__setitem__('DISPLAY',':0.0')

root = tkinter.Tk()
root.title("tester")
root.geometry("400x100")
lable = tkinter.Label(root,text="testing")
lable.pack()


root.mainloop