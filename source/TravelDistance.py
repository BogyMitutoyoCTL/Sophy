import LightBarrier
from TimeDifference import TimeDifference
import time
from datetime import datetime
from datetime import timedelta

class TravelDistance:
    def __init__(self, distance: int):
        self.difference = 0
        self.speed = 0
        self.distance = distance
        self.time_start = 0
        self.time_stop = 0


    def calculate_speed(self):
        self.speed = self.distance / self.difference
        self.speed = self.speed * 0.0036

    def calculate_difference(self):
        self.difference = TimeDifference().calculate(self.time_start, self.time_stop)

    def start(self, time):
        self.time_start = time


    def stop(self, time):
        self.time_stop = time
        self.calculate_difference()
        self.calculate_speed()



if __name__ == '__main__':
    a = TravelDistance(5)
    b = TravelDistance(10)
    c = TravelDistance(15)
    oben = LightBarrier.LightBarrier(4)
    oben.i_want_to_be_informed(a, "start")
    oben.i_want_to_be_informed(c, "start")
    mitte = LightBarrier.LightBarrier(17)
    mitte.i_want_to_be_informed(a, "stop")
    mitte.i_want_to_be_informed(b, "start")
    unten = LightBarrier.LightBarrier(27)
    unten.i_want_to_be_informed(b, "stop")
    unten.i_want_to_be_informed(c, "stop")



    time.sleep(10)

    print(a.difference)
    print(b.difference)
    print(c.difference)
