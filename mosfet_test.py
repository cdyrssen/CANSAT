import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(21, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(21, GPIO.LOW)
	time.sleep(3)
