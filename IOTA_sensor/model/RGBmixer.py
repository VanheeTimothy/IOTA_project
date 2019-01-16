from RPi import GPIO


class RGBmixer():

    def __init__(self, R,G,B):
        self.RGB = [R,G,B]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RGB, GPIO.OUT)

    def yellow(self):
        GPIO.output(self.RGB[0], GPIO.HIGH)
        GPIO.output(self.RGB[2], GPIO.HIGH)
        GPIO.output(self.RGB[1], GPIO.LOW)

    def magenta(self):
        GPIO.output(self.RGB[2], GPIO.LOW)
        GPIO.output(self.RGB[:2], GPIO.HIGH)

    def blue(self):
        GPIO.output(self.RGB, GPIO.LOW)
        GPIO.output(self.RGB[2], GPIO.HIGH)

    def red(self):
        GPIO.output(self.RGB, GPIO.LOW)
        GPIO.output(self.RGB[0], GPIO.HIGH)

    def green(self):
        GPIO.output(self.RGB, GPIO.LOW)
        GPIO.output(self.RGB[1], GPIO.HIGH)


    def ledOUT(self):
        GPIO.output(self.RGB, GPIO.LOW)

    def cleanUp(self):
        GPIO.cleanup()

