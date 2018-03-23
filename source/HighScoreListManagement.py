from HighScoreList import *
from HighScoreSave import *
from HighScoreEntry import *


class Management:
    def __init__(self,):
        self.Clients = []
        pass

    def manage(self, highscore: HighScoreList):
        self.Clients.append(highscore)

    def zuordnen(self, eintrag: HighScoreEntry):
        for liste in self.Clients:
            liste.add(eintrag)

    def speichern(self):

        HighScoreSave().save(self.Clients)

    def laden(self) -> bool:
        try:
            self.Clients = HighScoreSave().load()
            return True
        except:
            return False