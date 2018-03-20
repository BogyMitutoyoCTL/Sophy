from LightBarrier import LightBarrier
from TimeDifference import TimeDifference


class TravelDistance:
    def __init__(self, pinA: int, pinB: int, distance: int):
        self.difference = 0
        self.speed = 0
        self.pinA = pinA
        self.pinB = pinB
        self.distance = distance
        self.LB1 = LightBarrier(self.pinA).trigger()
        self.LB2 = LightBarrier(self.pinB).trigger()
        self.calculate_difference()
        self.calculate_speed()


    def calculate_speed(self):
        self.speed = self.distance / self.difference
        self.speed = self.speed * 0.0036

    def calculate_difference(self):
        self.difference = TimeDifference().calculate(self.LB1, self.LB2)





