import LightBarrier
import time
from HighScoreListManagement import *
from programm import *
import threading
import jsonpickle
import paho.mqtt.client as mqtt



class TravelDistance:
    def __init__(self, distance:int, management: Management, timeout: float):
        self.name = "Hans"
        self.entry_list = []
        self.timer_list = []
        self.distance = distance
        self.management = management
        self.timeout = timeout


    def start(self,time:float):
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
            pickle_copy = HighScoreEntry(None, None)
            pickle_copy.name = entry.name
            pickle_copy.distance = entry.distance / 1000
            pickle_copy.speed = format(entry.speed, ".2f")
            pickle_copy.duration = format(entry.duration, ".3f")
            entry_encode = jsonpickle.encode(pickle_copy)
            client = mqtt.Client()
            client.connect("localhost", 1883, 60)
            client.publish("newSpeed", entry_encode)
            client.disconnect()
        except:
            print("ERROR: Messung wurde noch nicht gestartet")




    def _on_timeout(self):
        print("Oops, I timed out")
        print("My timeout was {} seconds.".format(self.timeout))
        entry = self.entry_list[0]  # type: HighScoreEntry
        self.entry_list.remove(entry)
        timer = self.timer_list[0] # type: threading.Timer
        timer.cancel()
        self.timer_list.remove(timer)
