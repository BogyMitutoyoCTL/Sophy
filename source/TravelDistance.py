import LightBarrier
import time
from HighScoreListManagement import *
from programm import *
import datetime
import threading
import jsonpickle
import paho.mqtt.client as mqtt
from Statistik import *



class TravelDistance:
    def __init__(self, distance:int, management: Management, do_statistic: bool, timeout: float):
        self.name = ""
        self.entry_list = []
        self.timer_list = []
        self.distance = distance
        self.management = management
        self.timeout = timeout
        self.statistic = Statistik()
        self.do_statistic = do_statistic


    def start(self,time:float):
        mytime = datetime.now()
        print(mytime)
        self.name = mytime.strftime("%a - %H:%M:%S")
        entry = HighScoreEntry(str(self.name), self.distance)
        entry.start(time)
        self.entry_list.append(entry)

        timer = threading.Timer(self.timeout, self._on_timeout)
        timer.start()
        self.timer_list.append(timer)


    def stop(self,time:float):
        try:
            entry = self.entry_list[0] #type: HighScoreEntry
            timer = self.timer_list[0]  # type: threading.Timer
            entry.stop(time)
            timer.cancel()
            self.entry_list.remove(entry)
            self.timer_list.remove(timer)
            self.management.zuordnen(entry)
            self.management.speichern()

            if self.do_statistic == True:
                self.statistic.add(entry)

            pickle_copy = HighScoreEntry(None, None)
            pickle_copy.name = entry.name
            pickle_copy.distance = entry.distance
            pickle_copy.speed = entry.speed
            print(pickle_copy.speed)
            pickle_copy.duration = entry.duration
            entry_encode = jsonpickle.encode(pickle_copy)
            highscores = jsonpickle.encode(self.management.HighscoreListen[0])
            client = mqtt.Client()
            client.connect("localhost", 1883, 60)
            client.publish("newHighscore", highscores)
            print(highscores)
            client.publish("newSpeed", entry_encode)

            client.disconnect()
            print("Stop")
        except Exception as e:
            #print("ERROR: Messung wurde noch nicht gestartet")
            #print(e)
            pass


    def _on_timeout(self):
        print("Oops, I timed out")
        print("My timeout was {} seconds.".format(self.timeout))
        entry = self.entry_list[0]  # type: HighScoreEntry
        self.entry_list.remove(entry)
        timer = self.timer_list[0] # type: threading.Timer
        timer.cancel()
        self.timer_list.remove(timer)
