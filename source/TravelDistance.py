import LightBarrier
import time
from HighScoreListManagement import *
from programm import *


class TravelDistance:
    def __init__(self, distance:int, management: Management):
        self.name = "Hans"
        self.list = []
        self.distance = distance
        self.management = management



    def start(self,time:float):
        entry = HighScoreEntry(str(self.name), self.distance)
        entry.start(time)
        self.list.append(entry)


    def stop(self,time:float):
        entry = self.list[0] #type: HighScoreEntry
        entry.stop(time)
        self.list.remove(entry)
        self.management.zuordnen(entry)
        self.management.speichern()



