import RPi.GPIO as GPIO
import time

pin1 = 20
pin2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.HIGH)

while True:
	time.sleep(1)
