import RPi.GPIO as GPIO
import time
import random

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
servo_gpio = [13, 12]
GPIO.setup(servo_gpio, GPIO.OUT)

# Define servo preset positions
PRESETS = [
    {"z": -10, "y": 90},
    {"z": 125, "y": 50},
    {"z": 55, "y": 50},
    {"z": 55, "y": 130},
    {"z": 125, "y": 130},
]

# Set up PWM
pwm_frequency = 50  # Hz
z_pwm = GPIO.PWM(servo_gpio[0], pwm_frequency)
y_pwm = GPIO.PWM(servo_gpio[1], pwm_frequency)

def set_servo_position(preset_num):
    preset = PRESETS[preset_num]
    z_duty_cycle = calculate_duty_cycle(preset["z"])
    y_duty_cycle = calculate_duty_cycle(preset["y"])    
    z_pwm.start(z_duty_cycle)
    y_pwm.start(y_duty_cycle)
    print(preset_num)
    time.sleep(1)
    z_duty_cycle = calculate_duty_cycle(0)
    y_duty_cycle = calculate_duty_cycle(0)
    print(y_duty_cycle)
    z_pwm.start(z_duty_cycle)
    y_pwm.start(y_duty_cycle)
    time.sleep(1)

def calculate_duty_cycle(angle):
    duty_cycle = (angle / 18) + 2
    return duty_cycle

def get_preset_number():
    while True:
        try:
            preset_num = int(input("Enter the preset number (0-4): "))
            set_servo_position(preset_num)
            #list1 = [0, 1, 2, 3, 4]
            #print(random.choice(list1))
            #set_servo_position(random.choice(list1))
            #time.sleep(0.3)
        except ValueError:
            print("Invalid input. Please enter a number.")
            break


# Example usage
get_preset_number()

# Stop PWM and clean up GPIO
z_pwm.stop()
y_pwm.stop()
GPIO.cleanup()