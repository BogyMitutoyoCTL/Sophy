"""
Um die Werte für die Distanz, den Timeout und die Listeneinträge auszulesen oder zu generieren,
wurde eine Klasse erstellt, welche dies unter Hinzugabe von der entsprechenden Kategorie tut.
"""


class Persistence:
    def __init__(self, which_data):
        self.value = 0
        self.filePath = '../values/{}.md'.format(which_data)
        self.fileName = which_data
        try:
            with open(self.filePath, 'r') as file:
                file_content = file.read()
                self.set_value(file_content)
        except: self.save_to_file("0")

    def set_value(self, value):
        try:
            self.value = int(value)
        except:
            self.value=0

    def input_required(self):
        return self.value<=0

    def save_to_file(self, input: str) -> bool:
        self.set_value(input)
        try:
            with open(self.filePath, 'w') as file:
                file.write(str(self.value))
            return True
        except:
            return False
