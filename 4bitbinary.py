import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

no=(GPIO.input(36)<<3)+(GPIO.input(16)<<2)+(GPIO.input(15)<<1)+(GPIO.input(12))
print(no)
GPIO.cleanup()
