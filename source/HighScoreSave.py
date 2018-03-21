import jsonpickle


class HighScoreSave:
    def __init__(self):
        pass

    def save(self,ListOfEntry):
        list_of_entry_encode = jsonpickle.encode(ListOfEntry)

        with open("HighScoreSave.json", 'w') as file:
            file.write(list_of_entry_encode)

    def load(self):
        with open("HighScoreSave.json", 'r') as file:
            list_of_entry_decode = file.read()

        ListOfEntry = jsonpickle.decode(list_of_entry_decode)
        print("Ich hab geladen")

        return ListOfEntry


