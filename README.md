# PWM_Controller
A code repository that provides a GUI to the user to control PWM on specific pins. It uses Tkinter on Python, to work on the Raspberry Pi and Beaglebone platforms using RPi.GPIO and Adafruit_BBIO.PWM respectively.

# PWM_controller
A code repository that provides a GUI to the user to control PWM on specific pins. It uses Tkinter on Python, to work on the Raspberry Pi and Beaglebone platforms using RPi.GPIO and Adafruit_BBIO.PWM respectively.

The idea is to provide simple means of controlling the duty cycle of the PWM signals coming from the selected platform. There are only 4 PWM controllers available, but it can be expanded upon. The code layout should indicate quite clearly how it operates.

## Files
The repository contains 3 main files:
* **Base_GUI.py** - This is just the base files that can be run on any machine capable of executing python code. Mostly for debugging and experimenting.
* **PWM_Controller_Pi.py** - This is the code compilable and executable on the Raspberry Pi platform. Please follow the instructions below or the Setup instructions.txt
* **PWM_Controller_BB.py** - This is the code compilable and executable on the Beaglebone platform. Please follow the instructions below or the Setup instructions.txt

## Install guide for Linux platforms
The following instructions should be followed before trying to execute the code on the selected platform (Linux PC, Raspberry Pi, Beaglebone)
