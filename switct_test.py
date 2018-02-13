import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(21, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
