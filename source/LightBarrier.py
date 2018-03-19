import time
import RPi.GPIO as GPIO

GPIO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)


class LightBarrier:
    def __init__(self):
        self.first_time = 0
        self.second_time = 0

    def trigger(self):
        GPIO.wait_for_edge(GPIO_PIN, GPIO.RISING)
        self.first_time = time.time()


        GPIO.wait_for_edge(GPIO_PIN, GPIO.FALLING)

        GPIO.wait_for_edge(GPIO_PIN, GPIO.RISING)
        self.second_time = time.time()


LightBarrier1 = LightBarrier()
LightBarrier1.trigger()

LightBarrier2 = LightBarrier()
LightBarrier2.trigger()


print(signals.first_time)
print(signals.second_time)