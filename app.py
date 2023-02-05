import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
from capture import capture
from req import upload_file
from servoturn import turn_servo


def button_callback(channel):
    print(channel)
    print("Button was pushed!")
    capture()
    results = upload_file()
    print(results)
    #todo act on the results!!!
    #get the results
    #parse the json
    #get the prediction
    #turn the servo
    typeis = results['detected']
    turn_servo(typeis)

    
    # delay all other events for 1 second
    # this is to prevent multiple events from being triggered
    # when the button is held down
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(7, GPIO.RISING, callback=button_callback, bouncetime=2500)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up