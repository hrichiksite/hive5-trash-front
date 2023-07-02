import RPi.GPIO as GPIO
import time
import picamera
import requests

# GPIO pins for IR sensor and servo motors
IR_PIN = 13
SERVO_X_PIN = 12
SERVO_Z_PIN = 13

# Preset positions for servo motors
PRESETS = [
    {"z": 0, "y": 0},
    {"z": -35, "y": 35},
    {"z": -35, "y": -35},
    {"z": 35, "y": 35},
    {"z": 35, "y": -35},
]

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(SERVO_X_PIN, GPIO.OUT)
GPIO.setup(SERVO_Z_PIN, GPIO.OUT)
servo_x = GPIO.PWM(SERVO_X_PIN, 50)
servo_z = GPIO.PWM(SERVO_Z_PIN, 50)

# Start servo motors in base position
servo_x.start(7.5)
servo_z.start(7.5)
time.sleep(1)

# Function to take a picture with the webcam
def take_picture():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(2)
        camera.capture('/tmp/image.jpg')

# Function to send the picture to the API and get the classification
def classify_picture():
    url = 'https://your-api-url-here'
    files = {'image': open('/tmp/image.jpg', 'rb')}
    response = requests.post(url, files=files)
    return response.json()['classification']

# Function to set the servo motors to a preset position
def set_preset(preset):
    servo_x.ChangeDutyCycle(preset['y']/18.0 + 2.5)
    servo_z.ChangeDutyCycle(preset['z']/18.0 + 2.5)
    time.sleep(1)

# Main program loop
while True:
    if GPIO.input(IR_PIN):
        take_picture()
        classification = classify_picture()
        preset = PRESETS[classification]
        set_preset(preset)
