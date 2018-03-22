from tkinter import simpledialog as sdl

from CreateHighScoreEntry import *
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

    timeout = load_value("timeout")
    entries = load_value("entries")
    distance = load_value("distance")

    oben = LightBarrier.LightBarrier(4)
    mitte = LightBarrier.LightBarrier(17)
    creator = CreateHighScoreEntry()

    oben.i_want_to_be_informed(creator, "start")
    mitte.i_want_to_be_informed(creator, "stop")



