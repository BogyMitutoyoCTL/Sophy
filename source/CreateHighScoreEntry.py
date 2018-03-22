from HighScoreEntry import *
from HighScoreList import *
import LightBarrier
import time
from beeprint import pp


class CreateHighScoreEntry:
    def __init__(self):
        self.name = "Hans"
        self.list = []


    def start(self,time):
        entry = HighScoreEntry(str(self.name), 100)
        entry.start(time)
        self.list.append(entry)


    def stop(self,time):
        entry = self.list[0] #type: HighScoreEntry
        entry.stop(time)
        self.list.remove(entry)
        ListOfEntry.add(entry)

if __name__ == '__main__':
    max_number_of_entries = 4
    max_age = timedelta(days=7)
    ListOfEntry = HighScoreList(max_number_of_entries, max_age)
    oben = LightBarrier.LightBarrier(4)
    unten = LightBarrier.LightBarrier(17)
    creator = CreateHighScoreEntry()
    oben.i_want_to_be_informed(creator, "start")
    unten.i_want_to_be_informed(creator, "stop")


    time.sleep(5)

    pp(ListOfEntry)