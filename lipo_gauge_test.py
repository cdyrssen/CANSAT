import smbus
import time
import sys

I2C = smbus.SMBus(1)

while True:
	msb, lsb = I2C.read_byte_data(0x36, 0x02), I2C.read_byte_data(0x36, 0x03)
	perc = I2C.read_byte_data(0x36, 0x04)
	word = ((long(msb)<<8) + (long(lsb))) >> 4
	percent = float(word)/4095
	print word, perc
	time.sleep(0.5)
