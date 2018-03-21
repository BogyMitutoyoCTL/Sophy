import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)




class LightBarrier:
    def __init__(self, GPIO_PIN):
        self.time = 0
        self.GPIO_PIN = GPIO_PIN
        GPIO.setup(self.GPIO_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.GPIO_PIN, GPIO.RISING, callback= self.mycallback, bouncetime=200)

    def mycallback(self,GPIO_PIN):
        self.time = time.time()
        print(self.time)


if __name__ == '__main__':
    LightBarrier(4)
    time.sleep(10)


