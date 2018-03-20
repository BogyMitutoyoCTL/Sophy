class SpeedCalculation:
    def __init__(self,distance, time):
        self.distance = distance
        self.time = time
        self.speed = 0


    def speed_conversion(self):
        self.speed = self.distance / self.time  #Calculation of the speed in m/s
        self.speed = self.speed * 3.6           #Conversion of the speed in km/h
        return self.speed


if __name__ == '__main__':
    print("Geschwindigkeit: {}km/h".format(SpeedCalculation(9, 3).speed_conversion()))
