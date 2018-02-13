import numpy as np
import time
import RPi.GPIO as GPIO
import picamera
import Adafruit_BMP.BMP085 as BMP180
from mpu6050 import mpu6050

# GPIO Pins (Broadcom SoC numbering)
CHUTE_RELAY = 17
BUZZER = 

# Setup hardware interfaces
barometer = BMP180.BMP085()
motion_processor = mpu6050(0x68)
camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHUTE_RELAY, GPIO.OUT)
GPIO.output(CHUTE_RELAY, 0)

# Initialize variables
# --------------------
# Log blast transmission rate (Higher the number the slower the rate and more data sent per log)
log_blast_rate = 5

# Chute deployment altitude
altitude_threshold = 300

# Max measured difference for each sensor when resting
# AccelX | AccelY | AccelZ | GyroX | GyroY | GyroZ | Altitude | Pressure | Temperature | *GPS*
error_threshold = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]#gps error

# List of data entries in log
data = []

# Z acceleration magnitude when the rocket passes the deployment altitude
# during  ascension. When the magnitude becomes greater than this value we 
# know it has begun its descent and has passed the deployment altitude. 
z_magnitude = abs(motion_processor.get_accel_data()['z']

# Current and previous altitude readings
current_altitude = barometer.read_altitude()
previous_altitude = current_altitude

# Time stamp used to calculate ascension speed.
asc_time_stamp = time.time()
des_time_stamp = time.time()
ascension_speed = 0
descension_speed = 0

# Setup functions
# ---------------
# Test if current altitude is higher that the altitude to deploy chute
def above_threshold():
	previous_altitude = current_altitude
	current_altitude = barometer.read_altitude()
	if altitude_threshold < current_altitude:
		des_time_stamp = time.time()
		return True
	else:
		asc_time_stamp = time.time()
		return False

# Searches for point at which the falling speed is equal to the rising speed recorded at the
# time of breaking the altitude threshold to deploy chute.
def finding_deployment_point():
	descension_speed = (previous_altitude-current_altitude)/(time.time()-des_time_stamp)
	return ascension_speed > descension_speed

# Determines if the payload is resting or still in free-fall.
def resting():
	avg_data = np.array(data)
	avg_data = avg_data.sum(axis=0)
	avg_data = avg_data/len(data)
	error = abs(avg_data-data[-1])
	error_test = error < error_threshold
	return (error < error_threshold).sum() == len(error_threshold)

# Logs all sensor data and makes a new entry
def log_data():
	accel_data = motion_processor.get_accel_data()
	gyro_data = motion_processor.get_gyro_data()
	alt_data = barometer.read_altitude()
	press_data = barometer.read_pressure()
	temp_data = (barometer.read_temperature()+motion_processor.get_temp())/2
	#gps_data = gps.get_location()
	new_entry = [accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z'], alt_data, press_data, temp_data]#gps_data
	data.append(new_entry)

# Send logged data since last log transmission and clear data variable if successful
def send_logs():
	#serial.write(data)
	#if transmission successful:
		#data = []

# Tests if payload is resting and sends collected logs every # of entries specified in
# the log_blast_rate variable.
def logging():
	log_data()
	if data.len() % log_blast_rate == 0:
		send_logs()
		if resting():
			return False
		else:
			return True
	else:
		return True

# Deploy chute by switching relay pin HIGH to heat Nichrome wire and melt fishing line
def deploy_chute():
	GPIO.output(CHUTE_RELAY, 1)

# Begin program
# -------------
# Rocket is ascending in flight and has not broken the altitude at which to deploy chute.
while !above_threshold():

# Calculate the verticle speed at the point of breaking the altitude threshold
ascension_speed = (current_altitude-previous_altitude)/(time.time()-asc_time_stamp)

# Rocket has past the threshold to deploy chute, so start camera to capture chute
# deployment when rocket begins to fall back to Earth.
camera.start_recording('/home/pi/Desktop/descent.h264')

# Rocket deccelerates until it starts falling and begins to accelerate back to Earth.
while above_threshold() && finding_deployment_point():

# Rocket has passed the altitude threshold for a second time, this time
# in its descent, so the chute can be deployed.
deploy_chute()

# Begin logging
while logging():

# Payload has been determined to be resting on the ground, so stop
# the video recording.
camera.stop_recording()
