import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led =18

GPIO.setup(led, GPIO.OUT)

r=True
while r==True:
	GPIO.output(led, True)
	time.sleep(2)
	GPIO.output(led, False)
	time.sleep(2)