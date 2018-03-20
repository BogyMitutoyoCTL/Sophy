from LightBarrier import LightBarrier
from TimeDifference import TimeDifference
from TravelDistance import TravelDistance
from tkinter import *
from tkinter import simpledialog as sdl
from Persistence import Persistence


def load_value(s:str) -> Persistence:
    persistence = Persistence(s)
    if persistence.input_required():
        eingabe = sdl.askinteger("Enter value", persistence.fileName)
        save_ok = persistence.save_to_file(eingabe)
        if not save_ok:
            sdl.messagebox.showerror("ERROR", "{} not writeable".format(persistence.filePath))
    return persistence


if __name__ == '__main__':
    root = Tk()
    root.wm_title("Sophy")
    root.config(background = "#FFFFFF")

    leftFrame = Frame(root, width=200, height=400)
    leftFrame.grid(row=0, column= 0, padx=10, pady=3)

    rightFrame = Frame(root, width=400, height=400)
    rightFrame.grid(row=0, column=1, padx=10, pady=3)

    timeout = load_value("timeout")
    entries = load_value("entries")
    distance = load_value("distance")



    root.mainloop()