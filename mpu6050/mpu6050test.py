from mpu6050 import mpu6050

sensor = mpu6050(0x68)

accel, gyro, temp = sensor.get_all_data()

print 'Temperature: ', temp
print 'Accelerometer: ', accel
print 'Gyroscope: ', gyro
