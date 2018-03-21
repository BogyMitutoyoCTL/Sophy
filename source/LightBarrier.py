import time
import RPi.GPIO as GPIO
from TravelDistance import TravelDistance


GPIO.setmode(GPIO.BCM)




class LightBarrier:
    def __init__(self, GPIO_PIN):
        self.time = 0
        self.GPIO_PIN = GPIO_PIN
        self.distances = []
        self.commands = []
        GPIO.setup(self.GPIO_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.GPIO_PIN, GPIO.RISING, callback= self.intrrupt, bouncetime=200)

    def intrrupt(self, GPIO_PIN):
        self.time = time.time()
        for i in range(0, len(self.commands)):
            print("ich informiere jetzt {} über {}".format(self.distances[i], self.commands[i]))
            if  self.commands[i] == "start":
                 self.distances[i].start(self.time)
            if self.commands[i] == "stop":
                self.distances[i].stop(self.time)



    def i_want_to_be_informed(self, distance, command):
        self.distances.append(distance)
        self.commands.append(command)