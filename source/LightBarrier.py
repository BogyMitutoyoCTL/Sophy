import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class LightBarrier:
    def __init__(self, GPIO_PIN: int):
        self.GPIO_PIN = GPIO_PIN
        self.listener = []
        self.commands = []
        GPIO.setup(self.GPIO_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.GPIO_PIN, GPIO.RISING, callback= self.intrrupt, bouncetime=500)

    def intrrupt(self, GPIO_PIN):
        t = time.time()   #type: float
        for i in range(0, len(self.commands)):
            if  self.commands[i] == "start":
                self.listener[i].start(t)
            if  self.commands[i] == "stop":
                self.listener[i].stop(t)

    def i_want_to_be_informed(self, who, command):
        self.listener.append(who)
        self.commands.append(command)