"""
Um die Werte für die Distanz, den Timeout und die Listeneinträge auszulesen oder zu generieren,
wurde eine Klasse erstellt, welche dies unter Hinzugabe von der entsprechenden Kategorie tut.
"""

from tkinter import simpledialog as sdl
from tkinter import *

root = Tk()
root.withdraw()

class Persistence:
    def __init__(self, what_to_do):
        self.value = 0
        self.filePath = '../values/{}.md'.format(what_to_do)
        self.fileName = what_to_do

    def get_value(self):
        try:

            with open(self.filePath, 'r') as file:
                self.value = file.read()
                try:
                    self.value = int(self.value)
                except:
                    self.value = 0
        except:
            self.input_and_save()

        if self.value <= 0:
            self.input_and_save()

        return self.value

    def input_and_save(self):

        input = sdl.askinteger("WAS", self.fileName)
        try:
            with open(self.filePath, 'w') as file:
                file.write(str(input))
            self.value = input
        except:
            sdl.messagebox.showerror("ERROR", "{} not writeable".format(self.filePath))

distance = Persistence("distance").get_value()
timeout = Persistence("timeout").get_value()
entries = Persistence("entries").get_value()

print("Distance: {}".format(distance))
print("Timeout: {}".format(timeout))
print("Entries: {}".format(entries))