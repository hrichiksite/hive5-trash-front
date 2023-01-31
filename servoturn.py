import serial
from time import sleep

def turn_servo(preset):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    sleep(2)
    ser.write(bytes(str(preset), 'utf-8'))