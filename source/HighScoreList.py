from datetime import timedelta
from datetime import date
from HighScoreEntry import HighScoreEntry
from beeprint import pp
import jsonpickle
from HighScoreSave import *


class HighScoreList:

    def __init__(self, max_count: int, max_age: timedelta):
        self.list = []
        self.max_count = max_count
        self.max_age = max_age

    def add(self, newEntry):

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


'''Variables'''
max_number_of_entries = 3
max_age = timedelta(days=7)
ListOfEntry = HighScoreList(max_number_of_entries, max_age)

''' Entries '''
ListOfEntry.add(HighScoreEntry("Seva", timedelta(seconds=2, milliseconds=450), 44.2, date.today()))
ListOfEntry.add(HighScoreEntry("Thomas", timedelta(seconds=3, milliseconds=450), 24.3, date(2018, 3, 2)))
ListOfEntry.add(HighScoreEntry("Paul", timedelta(seconds=5, milliseconds=450), 37.3, date(2018, 3, 12)))
ListOfEntry.add(HighScoreEntry("Lukas", timedelta(seconds=1, milliseconds=450), 50.3, date(2018, 3, 18)))


a = HighScoreSave().save(ListOfEntry)

if __name__ == '__main__':

    ListOfEntry = HighScoreSave().load()

    pp(ListOfEntry)


