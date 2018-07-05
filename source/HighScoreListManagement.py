from HighScoreList import *
from HighScoreSave import *
from HighScoreEntry import *


class Management:
    def __init__(self,):
        self.HighscoreListen = []
        pass

    def manage(self, liste: HighScoreList):
        self.HighscoreListen.append(liste)

    def zuordnen(self, eintrag: HighScoreEntry):
        print(self.HighscoreListen)
        print(len(self.HighscoreListen))
        for liste in self.HighscoreListen:
            liste.add(eintrag)

    def speichern(self):

        HighScoreSave().save(self.HighscoreListen)

    def laden(self) -> bool:
        try:
            self.HighscoreListen = HighScoreSave().load()
            return True
        except:
            return False