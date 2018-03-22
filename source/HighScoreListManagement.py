from HighScoreList import *
from HighScoreSave import *
from HighScoreEntry import *
from CreateHighScoreEntry import *

Today = HighScoreList(3, timedelta(days=1))
Week = HighScoreList(5, timedelta(days=7))
Year = HighScoreList(7, timedelta(days=365))
Month = HighScoreList(5, timedelta(days=30))
eintrag = HighScoreEntry("Peter", 100)
eintrag.start(datetime(2018,3,22,13,44,0,0).timestamp())
eintrag.stop(datetime(2018,3,22,13,44,10,0).timestamp())



class Management:
    def __init__(self,):
        self.Clients = []
        pass

    def manage(self, highscore: HighScoreList):
        self.Clients.append(highscore)

    def zuordnen(self, eintrag: HighScoreEntry):
        for liste in self.Clients:
            liste.add(eintrag)

    def speichern(self, ):
        for liste in self.Clients:
            HighScoreSave().save(liste)


m = Management()
m.manage(Today)
m.manage(Week)
m.manage(Month)
m.manage(Year)
m.zuordnen(eintrag)
# rutschen

if __name__ == '__main__':
    m.speichern()