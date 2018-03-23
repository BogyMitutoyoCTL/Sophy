from tkinter import simpledialog as sdl
import LightBarrier
from TravelDistance import *
from Persistence import Persistence
from Statistik import *
from HighScoreListManagement import *
from beeprint import pp
from Signal import Signal
from ConsoleLogger import ConsoleLogger


def load_value(s:str) -> Persistence:
    persistence = Persistence(s)
    if persistence.input_required():
        eingabe = sdl.askinteger("Enter value", persistence.fileName)
        save_ok = persistence.save_to_file(eingabe)
        if not save_ok:
            sdl.messagebox.showerror("ERROR", "{} not writeable".format(persistence.filePath))
    return persistence


if __name__ == '__main__':


    s = Statistik()
    management = Management()
    Today = HighScoreList(3, timedelta(days=1))
    Week = HighScoreList(5, timedelta(days=7))
    Year = HighScoreList(7, timedelta(days=365))
    Month = HighScoreList(5, timedelta(days=30))
    management.manage(Today)
    management.manage(Week)
    management.manage(Month)
    management.manage(Year)
    management.manage(s)

    oben = LightBarrier.LightBarrier(4)
    mitte = LightBarrier.LightBarrier(17)
    unten = LightBarrier.LightBarrier(27)
    rot = Signal(22)
    gruen = Signal(10)
    gelb = Signal(9)
    log1 = ConsoleLogger("Es geht")


    creator1 = TravelDistance(250,management, 5)
    creator2 = TravelDistance(125,management, 5)
    oben.i_want_to_be_informed(creator1, "start")
    unten.i_want_to_be_informed(creator1, "stop")
    oben.i_want_to_be_informed(rot, "start")
    oben.i_want_to_be_informed(gruen, "stop")
    mitte.i_want_to_be_informed(rot, "stop")
    mitte.i_want_to_be_informed(gruen, "start")
    mitte.i_want_to_be_informed(log1, "start")

    time.sleep(20)
    s.save_to_file()
    pp(management.Clients)