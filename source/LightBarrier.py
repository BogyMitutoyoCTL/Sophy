import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


class LightBarrier:
    def __init__(self, GPIO_PIN):
        self.time = 0
        self.GPIO_PIN = GPIO_PIN

        GPIO.setup(self.GPIO_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)


    def trigger(self):
        GPIO.wait_for_edge(self.GPIO_PIN, GPIO.RISING)
        self.time = time.time()


        GPIO.wait_for_edge(self.GPIO_PIN, GPIO.FALLING)
        return self.time


