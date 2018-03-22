from HighScoreEntry import *
from HighScoreList import *
import LightBarrier
import time
from beeprint import pp
from HighScoreListManagement import *
from Statistik import *


class CreateHighScoreEntry:
    def __init__(self):
        self.name = "Hans"
        self.list = []


    def start(self,time:float):
        entry = HighScoreEntry(str(self.name), 100)
        entry.start(time)
        self.list.append(entry)


    def stop(self,time:float):
        entry = self.list[0] #type: HighScoreEntry
        entry.stop(time)
        self.list.remove(entry)
        m.zuordnen(entry)
        m.speichern()
        s.save_entry(entry)






if __name__ == '__main__':
    s = Statistik()
    m = Management()
    Today = HighScoreList(3, timedelta(days=1))
    Week = HighScoreList(5, timedelta(days=7))
    Year = HighScoreList(7, timedelta(days=365))
    Month = HighScoreList(5, timedelta(days=30))
    m.manage(Today)
    m.manage(Week)
    m.manage(Month)
    m.manage(Year)

    oben = LightBarrier.LightBarrier(4)
    mitte = LightBarrier.LightBarrier(17)


    creator = CreateHighScoreEntry()
    oben.i_want_to_be_informed(creator, "start")
    mitte.i_want_to_be_informed(creator, "stop")

    time.sleep(20)
    s.save_to_file()
    pp(m.Clients)
    pp(s.entries)