class load_distance:
    def __init__(self):
        self.distance = 0


    def load_file(self):
        fileName = '/home/pi/Sophy/values/distance.md'
        try:

            with open(fileName, 'r') as file:
                self.distance = file.read()
                try:
                    self.distance = int(self.distance)
                except:
                    self.distance = 0
        except:
            self.input_and_save(fileName)


        if self.distance  <= 0:
            self.input_and_save(fileName)


    def input_and_save(self, fileName):
        # TODO EINGABEFELD
        input = str(5)
        with open(fileName, 'w') as file:
            file.write(input)
        self.distance = int(input)


distance = load_distance()
distance.load_file()
print(distance.distance)
