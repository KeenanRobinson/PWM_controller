# PWM_Controller
A code repository that provides a GUI to the user to control PWM on specific pins. It uses Tkinter on Python, to work on the Raspberry Pi and Beaglebone platforms using RPi.GPIO and Adafruit_BBIO.PWM respectively.
_DISCLAIMER:_ I do not take responsibility for any damages that executing this code may cause, if setup incorrectly. 
* Please check you have set the correct pins and in the correct manner, with the right connections. Preferrably have them disconnected and use a voltmeter to check the voltage outputs first. Use a jumper wire to do this, as you risk connecting adjacent pin heads (like on the RPi, there are male pin headers) if you use the voltmeter probes. 
* Before connecting up, make sure you understand the maximum current rating for your platform for each pin and overall for your board. Typically you should not be powering circuits with PWM from a microprocessor, unless its a low power LED with some current limiting resistor or other very low power application.

## Files
The repository contains 3 main files:
* **Base_GUI.py** - This is just the base files that can be run on any machine capable of executing python code. Mostly for debugging and experimenting.
* **PWM_Controller_Pi.py** - This is the code compilable and executable on the Raspberry Pi platform. Please follow the instructions below.
* **PWM_Controller_BB.py** - This is the code compilable and executable on the Beaglebone platform. Please follow the instructions below.

## Install guide for Linux platforms
The following instructions should be followed before trying to execute the code on the selected platform (Linux PC, Raspberry Pi, Beaglebone):

### BEFORE YOU RUN:
1) This requires that your platform be connected to the internet, unless you have all the necessary libraries and such up to date. These parts are often helpful when dealing with Python programs. I have attached some URLs that I found useful for setting up virtual environments and running them, which you may want to do after Step 1 listed below.

Windows virtualenv:
Setting up: https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/
Activating/deactivating: https://www.codingforentrepreneurs.com/blog/activate-reactivate-deactivate-your-virtualenv

2) *Be sure of the pins you are using*

### 1) Install Python 3 and PIP

The version this script works with is Python 3.8.7, but should with any Python version compatible with tkinter.

For Linux systems, download using the following commands:

*sudo apt-get update*
*sudo apt-get install build-essential python3-dev python3-pip -y*

Once it has been installed, check the version using the command to see if installed correctly:

*python3 --version*

You should see the version printed in the command terminal.

### 2) Install Tkinter

This is the library that is used to develop the GUI. 

*pip install tk*

### 3) Download the platform specific libraries
Download the platform specific library, if you are using something other than the Base_GUI.py:

Raspberry Pi:
*sudo pip-3.2 install RPi.GPIO*

Beagebone:
*sudo pip3 install Adafruit_BBIO*

### 4) Configure the pins to setup

Instead of having to change the pins by editing to the code and recompiling, the pins must be changed using the pinSetup_(Board platform).txt. There you can also set the 
PWM frequency of the individual pins. Future revisions of the code can also be made to include change pins within the program, but for now I have it like this for simplicity.

### 5) Before FIRST runtime

Before you can make it an executable, run the following command in the Linux command line to compile and create an executable ( you should be in the directory of the Python code, otherwise you may want to add the directory path to the the upcoming commands):

_chmod +x (File name).py_

For example with the Beaglebone:

_chmod +x PWM_Controller_BB.py_

You can then run the executable by typing *without* the '.py'
_./(File name)_

UPDATE: You can also just execute the Python script directly using the following command:
_python (File name).py_

### 6) Run the executable file created
Use the following command to execute:

_./(File Name)_

For example with the Beaglebone:

_./PWM_Controller_BB_

## pinSetup and suggested pins
### pinSetup_x.txt
This is the 'config' file to use when you wish to change aspects of the pins. This may be the pin itself (first four entries) or the frequency (last four entries). Note the PWM frequency is in Hz.
### Raspberry Pi 3B+
These are some pins I recommend using for the Raspberry Pi 3B+. I do not know for any other versions what pins are available, so take care.
* GPIO12
* GPIO13
* GPIO18
* GPIO19

## Beaglebone Black
There are some pins to use for the Beaglebone Black. I have not tested these so take caution in selecting them, as some are connected to the same channel.
_DISCLAIMER: I have not tested this with a Beaglebone Black. This code was initially meant for a Beaglebone, but we moved away from using one before testing._
_Therefore, I accept no responsibility for potential damages and this implementation should be used with caution._

* P8_13
* P8_19
* P9_14
* P9_16
* P9_22 (NOTE: This is connected to SPI0_SLCK)
* P9_21 (NOTE: This is connected to SPI0_D0)
