import LightBarrier
from TimeDifference import TimeDifference
import time
from Signal import Signal
from ConsoleLogger import ConsoleLogger
from datetime import datetime

class TravelDistance:
    def __init__(self, distance: int):
        self.distance = distance
        self.time_start = 0 #type:datetime
        self.time_stop = 0 #type:datetime


    def calculate_speed(self,difference):
        self.speed = self.distance / difference
        self.speed = self.speed * 0.0036
        return self.speed

    def calculate_difference(self, time_start, time_stop,):
        self.difference = TimeDifference().calculate(time_start, time_stop)
        return self.difference

    def start(self, time):
        self.time_start = time

    def stop(self, time):
        self.time_stop = time
        self.calculate_difference()
        self.calculate_speed()


