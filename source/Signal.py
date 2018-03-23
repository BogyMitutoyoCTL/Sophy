import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Signal:
    def __init__(self,GPIO_PIN):
        self.GPIO_PIN = GPIO_PIN
        GPIO.setup(self.GPIO_PIN, GPIO.OUT)


    def start(self, time:float):
        GPIO.output(self.GPIO_PIN, GPIO.HIGH)

    def stop(self, time:float):
        GPIO.output(self.GPIO_PIN, GPIO.LOW)

