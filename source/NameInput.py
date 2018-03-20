from tkinter import *
from tkinter import simpledialog as sdl


class NameInput(sdl.Dialog):
    def __init__(self):
        self.__username = ""
        # self.e1

    def body(self, master):
        Label(master, text="User Name")
        self.e1 = Entry(master)
        return self.e1

    def apply(self):
        self.__username = self.e1.get()

    def getUsername(self):
        return self.__username

