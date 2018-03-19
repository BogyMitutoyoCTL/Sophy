
"""
Calculate time difference from two times
"""
from datetime import datetime
from datetime import timedelta


class TimeDifference:
    def __init__(self):
        pass

    def calculate(self, time1: datetime, time2: datetime) -> timedelta:
        return time2 - time1



