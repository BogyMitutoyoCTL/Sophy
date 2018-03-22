from datetime import timedelta
from datetime import date
from HighScoreEntry import HighScoreEntry


class HighScoreList:

    def __init__(self, max_count: int, max_age: timedelta):
        self.list = []
        self.max_count = max_count
        self.max_age = max_age

    def add(self, newEntry: HighScoreEntry):

        self.list.append(newEntry)

        ''' Remove old entries '''
        for entry in self.list:
            if date.today() - entry.record_date > self.max_age:
                self.list.remove(entry)

        ''' Sort (by the duration) '''
        self.list.sort()

        ''' Shorten (by the max number of entries) '''
        remove_count = len(self.list) - self.max_count
        for t in range(0, remove_count):
            self.list.pop(len(self.list)-1)