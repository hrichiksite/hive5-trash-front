from gpiozero import Servo
from time import sleep

servo_x = Servo(17)  # create servo object for X axis on GPIO 17
servo_y = Servo(27)  # create servo object for Y axis on GPIO 27

preset_1 = (0.12, 0)  # preset position 1: X=45, Y=45
preset_2 = (0.05, 0)  # preset position 2: X=90, Y=90
preset_3 = (0.05, 0.05)  # preset position 3: X=135, Y=135
preset_4 = (0.12, 0.05)  # preset position 4: X=180, Y=180
preset_5 = (0.09, 0.035)  # preset position 5: X=90, Y=90

current_preset = preset_5  # keep track of current preset position

def move_to_preset():
    servo_x.value = current_preset[0]  # move servo on X axis to preset position
    servo_y.value = current_preset[1]  # move servo on Y axis to preset position

# move to initial preset position
move_to_preset()

# loop to continuously check for new preset commands
while True:
    preset_number = int(input("Enter preset number (1 to 5): "))
    if preset_number == 1:
        current_preset = preset_1
    elif preset_number == 2:
        current_preset = preset_2
    elif preset_number == 3:
        current_preset = preset_3
    elif preset_number == 4:
        current_preset = preset_4
    elif preset_number == 5:
        current_preset = preset_5
    else:
        print("Invalid preset number. Try again.")
        continue
    move_to_preset()
    sleep(2)
    current_preset = preset_5  # move back to default position
    move_to_preset()
