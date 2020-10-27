import RPi.GPIO as GPIO
import time
import sys


class Dispenser:
    # define the gpios where the dispenser is connectes to
    dispenser_pin = 0

    # constructor
    # initialize the gpios you want to use
    def __init__(self, dispenser_gpio):

        # so you can use the gpio numbers of the raspberry pi
        GPIO.setmode(GPIO.BCM)
        
        # disable warnings
        GPIO.setwarnings(False)

        # define the gpios for output
        self.dispenser_pin = dispenser_gpio
        GPIO.setup(self.dispenser_pin, GPIO.OUT)

    
    # destructor
    # cleanup gpios after the usage of the dispenser
    def __del__(self):
        GPIO.cleanup()

    # liquid centiliter to time converter
    # you need to convert the amount of liquid in centiliter to time in seconds
    def convert_liquid_amount_to_time(self, cl):
        # needs improvement, we need to test!
        return float(cl * 1.5)

    def print_liquid_status(self, seconds, dispenser_number):
        cl = float(seconds) / 105
        for i in range(105):
            time.sleep(cl)
            if i % 5 == 0:
                sys.stdout.write(str(i) + "% ")
                sys.stdout.flush()
            if i % 100 == 0 and i > 0:
                sys.stdout.write("**** Dispenser on GPIO " + str(dispenser_number) + " is finished! ****\n")
                sys.stdout.flush()

    # trigger your dispenser
    # pass the number of the dispenser and the amount of liquid in cl (centiliter)
    def on(self, cl):
        if self.dispenser_pin == 18 or self.dispenser_pin == 23 or self.dispenser_pin == 24 or self.dispenser_pin == 25:
            GPIO.output(self.dispenser_pin, GPIO.HIGH)
            self.print_liquid_status(cl, self.dispenser_pin)
            GPIO.output(self.dispenser_pin, GPIO.LOW)
        else:
            print("Dispenser with the number " + str(self.dispenser_pin) + " does not exist!")
