import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

hallpin = 2
ledpin = 3

while True:
    if(gpio.input(hallpin) == False):
        gpio.output(ledpin, True)
        print("magnet detected")
    else:
        gpio.output(ledpin, False)
        print("magnetic field not detected")
