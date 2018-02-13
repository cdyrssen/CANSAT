import sys
import time
import pigpio

rx = 12
tx = 16

try:
	print 'Starting process'
	pi = pigpio.pi()
	pi.set_mode(rx, pigpio.INPUT)
	pi.set_mode(tx, pigpio.OUTPUT)

	pi.wave_clear()
	pi.wave_add_serial(tx,4800,'PSRF104,32.2159,-98.2159,388,0,159103,1985,12,1')
	wid = pi.wave_create()

	pi.wave_send_once(wid)
	pi.bb_serial_read_open(rx,4800,8) 
	
	print 'DATA - SOFTWARE SERIAL:'
	while True:	
		(count, data) = pi.bb_serial_read(rx)
		if count:
			print data
			time.sleep(0.25)
except:
	pi.bb_serial_read_close(rx)
	pi.stop()
