
from tkinter import simpledialog as sdl
import LightBarrier
from TravelDistance import *
from Statistik import *
from HighScoreListManagement import *
from beeprint import pp
from Signal import Signal
from ConsoleLogger import ConsoleLogger




if __name__ == '__main__':

    management = Management()



    if management.laden() == False:
        Today = HighScoreList(15, timedelta(days=1))
        Week = HighScoreList(5, timedelta(days=7))
        Year = HighScoreList(7, timedelta(days=365))
        Month = HighScoreList(5, timedelta(days=30))
        management.manage(Today)
        management.manage(Week)
        management.manage(Month)
        management.manage(Year)

    oben = LightBarrier.LightBarrier(17)
    mitte = LightBarrier.LightBarrier(4)


    rot = Signal(22)
    gruen = Signal(10)
    gelb = Signal(9)
    log1 = ConsoleLogger("Es geht")

    creator1 = TravelDistance(1.305, management, False,5)
    oben.i_want_to_be_informed(creator1, "start")
    oben.i_want_to_be_informed(rot, "start")
    oben.i_want_to_be_informed(gruen, "stop")
    oben.i_want_to_be_informed(log1, "start")

    mitte.i_want_to_be_informed(creator1, "stop")
    mitte.i_want_to_be_informed(rot, "stop")
    mitte.i_want_to_be_informed(gruen, "start")
    mitte.i_want_to_be_informed(log1, "stop")





    input("To quit the programm, press \"enter\"")


    creator1.statistic.save_to_file()
    pp(management.HighscoreListen)
