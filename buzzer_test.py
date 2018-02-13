import RPi.GPIO as GPIO

BUZZER = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

BUZZER_STATE = False

while True:
	raw_input('toggle pin')
	BUZZER_STATE = not BUZZER_STATE
	GPIO.output(BUZZER, BUZZER_STATE)
	
