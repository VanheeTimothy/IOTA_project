from RPi import GPIO



GPIO.setmode(GPIO.BCM)

RGB = [16,20,21]

GPIO.setup(RGB, GPIO.OUT)
GPIO.output(RGB[0], GPIO.LOW)

