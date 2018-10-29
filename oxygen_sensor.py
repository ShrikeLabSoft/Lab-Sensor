#######################################################################
#  Name:                 Oxygen Sensor Wireless
#  File Name:            oxygen_sensor.c    (To Be Defined)
#  Start Date:           22/October/2018
#  Developed by:         ShrikeLab
#  Programmer:           Andres Garcia Rubio
#  Experiment:           Algae
#  References:           Github link:
#  Language:             Python
#  Abstract:             Script for oxygen sensor using protocol TCP/IP
#  Hardware:             Raspberry Pi Zero W
#  IDE:                  Sublime Text
#######################################################################

import serial
import time
import csv
from gpiozero import LED
import RPi.GPIO as GPIO

green = LED(27)
red = LED(22)
toggleSwitch = 12

serial_handler = serial.Serial('/dev/ttyS0',9600,timeout=0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(toggleSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

number_samples = 0

while True:
    try:
        time.sleep(0.5)
        ser_bytes = serial_handler.readline()
        if(GPIO.input(toggleSwitch)):
          print("on")
          with open("/var/www/html/oxygendata.csv","a") as f:
            if(ser_bytes!=''):
              writer = csv.writer(f,delimiter=",")
              writer.writerow([time.time(),time.strftime("%a %d-%m-%Y @ %H:%M:%S"),ser_bytes])
              green.on()
              number_samples = number_samples + 1
              if(number_samples == 30):
                red.on()
        else:
          number_samples = 0
          print("off")
          green.off()
          red.off()

    except:
        print("Keyboard Interrupt")
        break
