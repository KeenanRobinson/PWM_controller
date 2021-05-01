# PWM_Controller
A code repository that provides a GUI to the user to control PWM on specific pins. It uses Tkinter on Python, to work on the Raspberry Pi and Beaglebone platforms using RPi.GPIO and Adafruit_BBIO.PWM respectively.

## Files
The repository contains 3 main files:
* **Base_GUI.py** - This is just the base files that can be run on any machine capable of executing python code. Mostly for debugging and experimenting.
* **PWM_Controller_Pi.py** - This is the code compilable and executable on the Raspberry Pi platform. Please follow the instructions below or the Setup instructions.txt
* **PWM_Controller_BB.py** - This is the code compilable and executable on the Beaglebone platform. Please follow the instructions below or the Setup instructions.txt

## Install guide for Linux platforms
The following instructions should be followed before trying to execute the code on the selected platform (Linux PC, Raspberry Pi, Beaglebone):

###BEFORE YOU RUN:
This requires that your platform be connected to the internet. These parts are often helpful when dealing with Python programs. I have attached some URLs that I found useful for setting up virtual environments and running them, which you may want to do after Step 1 listed below.

Windows virtualenv:
Setting up: https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/
Activating/deactivating: https://www.codingforentrepreneurs.com/blog/activate-reactivate-deactivate-your-virtualenv

###1) Install Python 3 and PIP

The version this script works with is Python 3.8.7, but should with any Python version compatible with tkinter.

For Linux systems, download using the following commands:

*sudo apt-get update*
*sudo apt-get install build-essential python3-dev python3-pip -y*

Once it has been installed, check the version using the command to see if installed correctly:
*python --version*

OR

*python3 --version*

###2) Install Tkinter

This is the library that is used to develop the GUI. 

*pip install tk*

###3) Download the platform specific libraries
Download the platform specific library, if you are using something other than the Base_GUI.py:

Raspberry Pi:
*sudo pip-3.2 install RPi.GPIO*

Beagebone:
*sudo pip3 install Adafruit_BBIO*

###4) Configure the pins to setup

Instead of having to change the pins by editing to the code and recompiling, the pins must be changed using the pinSetup_<Board platform>.txt. There you can also set the 
PWM frequency of the individual pins. Future revisions of the code can also be made to include change pins within the program, but for now I have it like this for simplicity.

###5) Before FIRST runtime

Before you can make it an executable, run the following command in the Linux command line to compile and create an executable:

*chmod +x <File name>.py*
For example with the Beaglebone:
*chmod +x PWM_Controller_BB.py*

###5) Run the executable file created
Use the following command to execute:

*./<File Name>*
For example with the Beaglebone:
*./PWM_Controller_BB*
