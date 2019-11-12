import RPi.GPIO as gpio, time
from gpiozero import LED, Button
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

hallpin = Button(17)
ledpin = LED(27)

while True:
    if hallpin.is_pressed:
        ledpin.on()
        print("magnet detected")
    else:
        ledpin.off()
        print("magnetic field not detected")
