import Adafruit_BMP.BMP085 as BMP180
from mpu6050 import mpu6050
import picamera
import time
import numpy as np

barometer = BMP180.BMP085()
motion_processor = mpu6050(0x68)

num_entries = 100
data = [None]*num_entries
accel_x_str = '\tAccelerometer x\t\t-\t'
accel_y_str = '\tAccelerometer y\t\t-\t'
accel_z_str = '\tAccelerometer z\t\t-\t'
gyro_x_str = '\tGyroscope x\t\t-\t'
gyro_y_str = '\tGyroscope y\t\t-\t'
gyro_z_str = '\tGyroscope z\t\t-\t'
alt_str = '\tAltitude\t\t-\t'
press_str = '\tPressure\t\t-\t'
temp_str = '\tTemperature\t\t-\t'

#camera = picamera.PiCamera()
#camera.start_recording('/home/pi/Desktop/test.h264')

time_stamp = time.time()
file = ''

for i in range(num_entries):
	accel_data = motion_processor.get_accel_data()
        gyro_data = motion_processor.get_gyro_data()
        alt_data = barometer.read_altitude()
        press_data = barometer.read_pressure()
        temp_data = (barometer.read_temperature()+motion_processor.get_temp())/2
        #gps_data = gps.get_location()
        new_entry = [accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z'], alt_data, press_data, temp_data]
        data[i] = new_entry

	'''with open('test.txt', 'r') as f:
		file = f.read()
		f.close()

	file = file + '\n' + str(data[i])

	with open('test.txt', 'w') as f:
		f.write(str(file))
		f.close()'''

total_time = time.time()-time_stamp

#camera.stop_recording()

print 'Time to log ', num_entries, ' entries: ', int(total_time)/60, ' minute(s), ', round(total_time%60, 2), ' second(s)'
print 'Number Entries per second: ', round(num_entries/total_time,2)
print

data = np.array(data)
avg = data.sum(axis=0)/len(data)
max_vals = np.amax(data, axis=0)
min_vals = np.amin(data, axis=0)
variance = max_vals-min_vals
over_shoot_error = max_vals-avg
under_shoot_error = avg-min_vals

print 'Maximum variance: '
print accel_x_str, round(variance[0],5)
print accel_y_str, round(variance[1],5)
print accel_z_str, round(variance[2],5)
print gyro_x_str, round(variance[3],5)
print gyro_y_str, round(variance[4],5)
print gyro_z_str, round(variance[5],5)
print alt_str, round(variance[6],5)
print press_str, round(variance[7],5)
print temp_str, round(variance[8],5)
print
print 'Over shoot error: '
print accel_x_str, round(over_shoot_error[0],5)
print accel_y_str, round(over_shoot_error[1],5)
print accel_z_str, round(over_shoot_error[2],5)
print gyro_x_str, round(over_shoot_error[3],5)
print gyro_y_str, round(over_shoot_error[4],5)
print gyro_z_str, round(over_shoot_error[5],5)
print alt_str, round(over_shoot_error[6],5)
print press_str, round(over_shoot_error[7],5)
print temp_str, round(over_shoot_error[8],5)
print
print 'Under shoot error: '
print accel_x_str, round(under_shoot_error[0],5)
print accel_y_str, round(under_shoot_error[1],5)
print accel_z_str, round(under_shoot_error[2],5)
print gyro_x_str, round(under_shoot_error[3],5)
print gyro_y_str, round(under_shoot_error[4],5)
print gyro_z_str, round(under_shoot_error[5],5)
print alt_str, round(under_shoot_error[6],5)
print press_str, round(under_shoot_error[7],5)
print temp_str, round(under_shoot_error[8],5)
print '-----------------------------------------------'
print
