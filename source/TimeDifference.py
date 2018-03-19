
"""
Calculate time difference from two times
"""


class TimeDifference:
    def __init__(self):
        pass

    def calculate(self, time1, time2):
        difftime = time2 - time1
        print(time1.strftime("%b %d %Y %H:%M:%S:%f"))
        print(time2.strftime("%b %d %Y %H:%M:%S:%f"))
        # print(str(difftime.microseconds / 1000))
        print(str(difftime))


