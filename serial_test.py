import serial

port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=3.0)

while True:
	port.write('Hello Michael\n')
	raw_input('send again')

