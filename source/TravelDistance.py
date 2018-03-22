import LightBarrier
import time
from beeprint import pp
import LightBarrier
from HighScoreListManagement import *
from Statistik import *
from TravelDistance import *


class TravelDistance:
    def __init__(self, distance:int):
        self.name = "Hans"
        self.list = []
        self.distance = distance


    def start(self,time:float):
        entry = HighScoreEntry(str(self.name), self.distance)
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
    untenen = LightBarrier.LightBarrier(27)

    creator1 = TravelDistance(250)
    creator2 = TravelDistance(125)
    oben.i_want_to_be_informed(creator1, "start")
    mitte.i_want_to_be_informed(creator1, "stop")



    time.sleep(20)
    s.save_to_file()
    pp(m.Clients)
    pp(s.entries)