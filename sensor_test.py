import Adafruit_BMP.BMP085 as BMP180
from mpu6050 import mpu6050

barometer = BMP180.BMP085()
motion_processor = mpu6050(0x68)
user_input = 'y'

while user_input == 'y':
	print 'Pressure: ', barometer.read_pressure()
	print 'Altitude: ', barometer.read_altitude()
	print 'Temperature: ', (barometer.read_temperature()+motion_processor.get_temp())/2
	print 'Accelerometer:'
	accel_data = motion_processor.get_accel_data()
	print '\tx - ', accel_data['x']
	print '\ty - ', accel_data['y']
	print '\tz - ', accel_data['z']
	print 'Gyroscope:'
	gyro_data = motion_processor.get_gyro_data()
	print '\tx - ', gyro_data['x']
	print '\ty - ', gyro_data['y']
	print '\tz - ', gyro_data['z']
	print
	user_input = raw_input('Get more data [y/n]? ')
	print '----------------------------------------'
	print
