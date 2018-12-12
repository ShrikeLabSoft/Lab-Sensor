# Lab-Sensor
Simple lab sensor implemented using Iot

The main program is a python script saved in the home folder and [run from a call in the /etc/rc.local folder](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/) in order to start the script when the RPi is turned on.

In case there is no wireless internet access available, the RPi zero W can be connected via ethernetto a computer using a micro usb cable [using this method](https://www.thepolyglotdeveloper.com/2016/06/connect-raspberry-pi-zero-usb-cable-ssh/)

Python libraries needed for this raspberry pi project:

* matplotlib
* serial
* pycairo
* csv
* serial
* gpiozero
* gpiozero
* random


# Hardware Used

A Raspberry Pi Zero was used for this project. A [Dissolved Oxygen Sensor](https://www.atlas-scientific.com/product_pages/kits/do_kit.html) from Atlas Scientific was used to detect oxygen levels. The time of the samples and the oxygen level was saved in a .csv file.

Two LEDs were used alongside the sensor as indicators of how many samples have been taken. A simple pull-down switch was used to start and stop taking samples.

# Software Used

A LAMP [Linux Apache Mysql PHP] (https://www.atlas-scientific.com/product_pages/kits/do_kit.html) environment was set up for the raspberry pi running as a server. the webpage has a basic download link for the file
