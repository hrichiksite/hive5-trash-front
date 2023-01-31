import serial
from time import sleep

ser = serial.Serial('/dev/ttyAMA0', 9600)

ser.write(b'1')