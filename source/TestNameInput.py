from tkinter import *
from tkinter import simpledialog as sdl
from NameInput import NameInput

root = Tk()
top = Toplevel()


def helloCallBack():
    result = sdl.askstring("Enter Name", "Name")
    print(result)


def TestCallBack():
    result = NameInput()
    result.body(root)


B = Button(root, text ="Hello", command = helloCallBack)
C = Button(root, text ="Test", command = TestCallBack)

C.pack()
B.pack()
root.mainloop()

