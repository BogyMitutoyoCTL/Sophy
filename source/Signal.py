import RPi.GPIO as GPIO


class Signal:
    def __init__(self,GPIO_PIN):
        self.GPIO_PIN = GPIO_PIN
        GPIO.setup(self.GPIO_PIN, GPIO.OUT)


    def start(self, time):
        GPIO.output(self.GPIO_PIN, GPIO.HIGH)

    def stop(self, time):
        GPIO.output(self.GPIO_PIN, GPIO.LOW)

