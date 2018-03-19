import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)      #PIN_MAPPING



class LightBarrier:
    def __init__(self, GPIO_PIN):
        self.time = 0
        self.GPIO_PIN = GPIO_PIN
        GPIO.setup(self.GPIO_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

    def trigger(self):
        GPIO.wait_for_edge(self.GPIO_PIN, GPIO.RISING)
        self.time = time.time()


        GPIO.wait_for_edge(self.GPIO_PIN, GPIO.FALLING)



LightBarrier1 = LightBarrier(4)
LightBarrier1.trigger()


LightBarrier2 = LightBarrier(17)
LightBarrier2.trigger()

print(LightBarrier1.time)
print(LightBarrier2.time)