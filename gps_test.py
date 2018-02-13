import pigpio
import time
import commands

rx=18
tx=17
led = 23

tmp = [0]*300

try:
#	print commands.getoutput('sudo pigpiod')
	pi = pigpio.pi()
	pi.set_mode(rx, pigpio.INPUT)
	pi.set_mode(tx, pigpio.OUTPUT)
	pi.set_mode(led, pigpio.OUTPUT)

	pi.bb_serial_read_open(rx,4800,8)

	pi.write(led, 1)

	for i in range(10):
		(count, data) = pi.bb_serial_read(rx)
		if count:
			tmp[i] = data
			time.sleep(0.5)

	pi.write(led, 0)

	with open('/home/pi/Documents/CANSAT/gps_data.txt', 'w') as f:
		f.write(str(tmp))
		f.close()
except:
	for i in range(3):
		pi.write(led, 1)
		time.sleep(1)
		pi.write(led, 0)
		time.sleep(1)
	pi.stop()
