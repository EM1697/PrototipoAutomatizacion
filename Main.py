import os, glob, time, datetime
import RPi.GPIO as gpio
from gpiozero import LED, Button
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Pagina de Sensor de Temp = http://www.innovadomotics.com/mn-tuto/mn-mod/mn-rp/11-raspberry-pi-ds18b20.html

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

_direccion = '/sys/bus/w1/devices/'
dispositivo_folder = glob.glob(_direccion + '28*')[0]
dispositivo_pad = dispositivo_folder + '/w1_slave'

hallpin = Button(17)
ledpin = LED(27)

print("Setup GPIO pin as input on GPIO17")

# Set Switch GPIO as input
# Pull high by default
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
#gpio.add_event_detect(17, gpio.BOTH, callback=sensorCallback, bouncetime=200)

# Funciones
def leer_temperatura():
    f = open(dispositivo_pad, 'r')
    lineas = f.readlines()
    f.close()
    return lineas


def determinar_valores():
    lineas = leer_temperatura()
    while lineas[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lineas = leer_temperatura()
    igual_pos = lineas[1].find('t=')
    if igual_pos != -1:
        temp_string = lineas[1][igual_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

# Magic
try:
    while True:
         # Called if sensor output changes
        timestamp = time.time()
        stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    	if gpio.input(17):
        # No magnet
#        	print("Sensor HIGH " + stamp)
		ledpin.on()
    	else:
        	# Magnet
	        #print("Sensor LOW " + stamp)
		ledpin.off()

        print("centigrados,fahrenheit")
        print(determinar_valores())
        time.sleep(0.0000000000001)
except KeyboardInterrupt:
    # Reset GPIO settings
    gpio.cleanup()
