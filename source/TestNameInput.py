from tkinter import *
from tkinter import simpledialog as sdl


top = Tk()

def helloCallBack():
    result = sdl.askstring("Enter Name", "Name")
    print(result)


B = Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

