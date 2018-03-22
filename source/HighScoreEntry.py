"""
HighScoreEntry: Information required for an entry in the high score list.
This is just a data container. This class cannot do something.
"""
from datetime import timedelta
from datetime import datetime
from datetime import date
from TimeDifference import *


class HighScoreEntry:
    def __init__(self, name: str, distance: int):
        """
        Initializes the data class with all available values.
        :param name: Name of the object or person holding the record.
        :param duration: Time needed to pass all light barriers.
                         This value can be used for sorting the high score list.
        :param speed: Speed in km/h, calculated from the duration and the distance of the light barriers.
                      This value is probably better understood by humans compared to duration.
        :param record_date: Date when the record was achieved.
                            This value can be used for building a weekly, monthly and all-time
                            high score list
        """
        self.name = name
        self.duration = 0
        self.speed = 0
        self.record_date = 0 #type: date
        self.start_time = 0 #type: datetime
        self.stop_time = 0 #type: datetime
        self.distance = distance

    ''' Functions to sort the entries '''
    def __lt__(self, other):            #less then
            return self.duration < other.duration

    def __eq__(self, other):            #equal
            return self.duration == other.duration

    def start(self,time):
        self.start_time = time


    def stop(self,time):
        self.stop_time = time
        self.record_date = date.fromtimestamp(self.stop_time)
        self.duration = self.calculate_difference(self.start_time, self.stop_time)
        self.speed = self.calculate_speed(self.duration)

    def calculate_speed(self,difference):
        self.speed = self.distance / difference
        self.speed = self.speed * 0.0036
        return self.speed

    def calculate_difference(self, time_start, time_stop,):
        self.duration = TimeDifference().calculate(time_start, time_stop)
        return self.duration

