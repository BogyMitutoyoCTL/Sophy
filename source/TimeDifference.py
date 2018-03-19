

class TimeDifference:
    def __init__(self):
        self.description = "Calculate time difference from two times"

    def calculate(self, time1, time2):
        print(time1.strftime("%b %d %Y %H:%M:%S:%f"))
        print(time2.strftime("%b %d %Y %H:%M:%S:%f"))


