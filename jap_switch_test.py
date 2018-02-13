import RPi.GPIO as GPIO
import time


pin1 = 4
pin2 = 17
pin3 = 27
pin4 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

while True:
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)


