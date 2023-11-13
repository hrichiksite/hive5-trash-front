import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
from capture import capture
#from servo import set_servo_position
import requests
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set up GPIO pins
servo_gpio = [33, 32]
GPIO.setup(servo_gpio, GPIO.OUT)

# Define servo preset positions
PRESETS = [
    {"z": 90, "y": 90},
    {"z": 125, "y": 50},
    {"z": 55, "y": 50},
    {"z": 55, "y": 130},
    {"z": 125, "y": 130},
]

# Set up PWM
pwm_frequency = 50  # Hz
#z_pwm = GPIO.PWM(servo_gpio[0], pwm_frequency)
#y_pwm = GPIO.PWM(servo_gpio[1], pwm_frequency)

def set_servo_position(preset_num):
    z_pwm = GPIO.PWM(servo_gpio[0], pwm_frequency)
    y_pwm = GPIO.PWM(servo_gpio[1], pwm_frequency)
    preset = PRESETS[preset_num]
    z_duty_cycle = calculate_duty_cycle(preset["z"])
    y_duty_cycle = calculate_duty_cycle(preset["y"])    
    z_pwm.start(z_duty_cycle)
    y_pwm.start(y_duty_cycle)
    print(preset_num)
    time.sleep(3)
    z_duty_cycle = calculate_duty_cycle(90)
    y_duty_cycle = calculate_duty_cycle(90)
    print(y_duty_cycle)
    z_pwm.start(z_duty_cycle)
    y_pwm.start(y_duty_cycle)
    time.sleep(1)
    z_pwm.stop()
    y_pwm.stop()

def calculate_duty_cycle(angle):
    duty_cycle = (angle / 18) + 2
    return duty_cycle


API_URL = "https://api-inference.huggingface.co/models/pyesonekyaw/recycletree_materials"
headers = {"Authorization": "Bearer {REPLACE_WITH_HF_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    if response.status_code != 200:
        print('retry')
        sleep(3)
        return False
    else:
        return response.json()

def button_callback(channel):
    time.sleep(0.1)  # Add a small delay to debounce the button

    if GPIO.input(channel) == GPIO.LOW:
        print('rejected')
        return
    print(channel)
    print("Button was pushed!")
    capture()
    results = query('trash.jpg')
    i = 0
    while results == False & i < 5:
        results= query('trash.jpg')
    print(results)
    #todo act on the results!!!
    #get the results
    #parse the json
    #get the prediction
    #turn the servo
    typeis = results[0]['label']
    if(typeis == 'plastic'):
        set_servo_position(1)
    elif(typeis == 'paper'):
        set_servo_position(2)
    elif(typeis == 'glass'):
        set_servo_position(3)
    elif(typeis == 'metal'):
        set_servo_position(4)
    elif(typeis == 'others'):
        set_servo_position(4)


    
    # delay all other events for 1 second
    # this is to prevent multiple events from being triggered
    # when the button is held down
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(15, GPIO.RISING, callback=button_callback, bouncetime=1000)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
