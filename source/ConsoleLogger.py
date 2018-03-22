from datetime import datetime

class ConsoleLogger:
    def __init__(self, what):
        self.what = what

    def start(self,time:float):
        d = datetime.fromtimestamp(time)
        print("Zur Uhrzeit {} ist {} gestartet.".format(d, self.what))

    def stop(self,time:float):
        x = datetime.fromtimestamp(time)
        print("Zur Uhrzeit {} ist {} gestoppt.".format(x, self.what))
