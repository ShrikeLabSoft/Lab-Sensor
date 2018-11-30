import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

import serial
import time
import csv
from gpiozero import LED
import RPi.GPIO as GPIO

#hardware constants declarations
green = LED(27)
red = LED(22)
toggleSwitch = 12

#serial bus declaration
serial_handler = serial.Serial('/dev/ttyS0',9600,timeout=0)

#Settings for GPIO and serial bus
GPIO.setmode(GPIO.BCM)
GPIO.setup(toggleSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Parameters
x_len = 50         # Number of points to display
y_range = [0, 20]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 50))
ys = [0] * x_len
ax.set_ylim(y_range)


# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('Oxygen Level Sensor')
plt.xlabel('Samples')
plt.ylabel('Oxygen lvl mg/L')

num = 0

# This function is called periodically from FuncAnimation
def animate(i, ys):


    num = 9
    
    ser_bytes = serial_handler.readline()

    if(len(ser_bytes) > 3):
        num = float(ser_bytes[0:4])


    temp_c = num

    # Add y to list
    ys.append(temp_c)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=500,
    blit=True)
plt.show()
