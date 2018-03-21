"""
HighScoreEntry: Information required for an entry in the high score list.
This is just a data container. This class cannot do something.
"""
from datetime import timedelta
from datetime import date


class HighScoreEntry:
    def __init__(self, name: str, duration: timedelta, speed: float, record_date: date):
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
        self.duration = duration
        self.speed = speed
        self.record_date = record_date

    ''' Functions to sort the entries '''
    def __lt__(self, other):            #less then
            return self.duration < other.duration

    def __eq__(self, other):            #equal
            return self.duration == other.duration
