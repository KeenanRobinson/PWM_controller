#*******************************************************************
#                           DESCRIPTION                 
# The following code is a base GUI to allow users to control the     
# duty cycle of 4 PWM pins on the Raspberry Pi. It has been tested 
# and works on on the 3B+, with Python 3.8.7 and 3.x.x 
#
# Please read the README for details on its operation. Settings are
# configured in a text file.
#
# Date created: 01/05/2021
# Created by: Keenan Robinson
# ******************************************************************                   

from Tkinter import *
import sys
import RPi.GPIO as GPIO #RPI setting

#************************************
#       VARIABLE DEFINTIONS         *

mainWindow = Tk() # Creates the root window object
mainWindow.title("Raspberry Pi PWM Controller")
mainWindow.geometry("640x250+20+20") #width x height + XPOS + YPOS
filename= "pinSetup_Pi.txt"
GPIO.setmode(GPIO.BCM) #RPI setting: pins are BCM numbering

#   END OF VAR. DEFINITIONS         *
#************************************
def mainWindowSetup(): # Sets up the main window with widgets
    #GUI constants for positioning
    generalPadx = 5
    generalPady = 5
    scalePadx =5
    scalePady =5
    scaleIPadx=2
    scaleIPady=30 #Increase this to increase scale length
    entryWidth=10  #Increase this increases Entry widget size

    #Duty cycle values to update widgets
    dutyCycle0 = IntVar()
    dutyCycle1 = IntVar()
    dutyCycle2 = IntVar()
    dutyCycle3 = IntVar()

    global pwm0 # Unfortunately with the way arguments are passed, this must be global
    global pwm1
    global pwm2
    global pwm3
    #RPI Settings: Configure pins
    pins, pinFrequency = readPinSetup()
    GPIO.setup(pins[0], GPIO.OUT) #RPI setting: GPIO.output(pin, GPIO.MODE)
    pwm0 = GPIO.PWM(pins[0], pinFrequency[0]) #RPI Setting: GPIO.PWM(pin, frequency)
    GPIO.setup(pins[1], GPIO.OUT)
    pwm1 = GPIO.PWM(pins[1], pinFrequency[1])
    GPIO.setup(pins[2], GPIO.OUT)
    pwm2 = GPIO.PWM(pins[2], pinFrequency[2])
    GPIO.setup(pins[3], GPIO.OUT)
    pwm3 = GPIO.PWM(pins[3], pinFrequency[3])
    pwm0.start(0) #RPI setting: pwm.start(initialDutyCycle)
    pwm1.start(0)
    pwm2.start(0)
    pwm3.start(0)
    #RPI settings end

    #Create label widgets
    pwmLabel0 = Label(mainWindow, text="PWM0")
    pwmLabel1 = Label(mainWindow, text="PWM1")
    pwmLabel2 = Label(mainWindow, text="PWM2")
    pwmLabel3 = Label(mainWindow, text="PWM3")

    #Create entry widgets
    pwmInput0 = Entry(mainWindow, textvariable =dutyCycle0, width=entryWidth)
    pwmInput1 = Entry(mainWindow, textvariable =dutyCycle1, width=entryWidth)
    pwmInput2 = Entry(mainWindow, textvariable =dutyCycle2, width=entryWidth)
    pwmInput3 = Entry(mainWindow, textvariable =dutyCycle3, width=entryWidth)

    #Create button widgets
    button0 = Button(mainWindow,text="Set Duty Cycle [0]",command=lambda: pwm0.ChangeDutyCycle(dutyCycle0.get()))
    button1 = Button(mainWindow,text="Set Duty Cycle [1]",command=lambda: pwm1.ChangeDutyCycle(dutyCycle1.get())) 
    button2 = Button(mainWindow,text="Set Duty Cycle [2]",command=lambda: pwm2.ChangeDutyCycle(dutyCycle2.get())) 
    button3 = Button(mainWindow,text="Set Duty Cycle [3]",command=lambda: pwm3.ChangeDutyCycle(dutyCycle3.get()))

    #Create scale (sliders)
    pwm0Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle0, orient='vertical', command=lambda x: pwm0.ChangeDutyCycle(dutyCycle0.get()))
    pwm1Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle1, orient='vertical', command=lambda x: pwm1.ChangeDutyCycle(dutyCycle1.get()))
    pwm2Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle2, orient='vertical', command=lambda x: pwm2.ChangeDutyCycle(dutyCycle2.get()))
    pwm3Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle3, orient='vertical', command=lambda x: pwm3.ChangeDutyCycle(dutyCycle3.get()))

    #Grid geometry handler to layout the GUI
    #PWM0:
    pwmLabel0.grid(row = 1, column = 0, sticky = W,  pady = generalPady, padx = generalPadx)
    pwmInput0.grid(row = 1, column = 1, sticky = W,  pady = generalPady)
    pwm0Scale.grid(row = 0, column = 0, sticky = '', pady = scalePady, ipady=scaleIPady, columnspan = 2)
    button0.grid  (row = 2, column = 0, sticky = '', pady = generalPady, padx = generalPadx, columnspan = 2)
    #PWM1:
    pwmLabel1.grid(row = 1, column = 2, sticky = W,  pady = generalPady, padx = generalPadx)
    pwmInput1.grid(row = 1, column = 3, sticky = W,  pady = generalPady)
    pwm1Scale.grid(row = 0, column = 2, sticky = '', pady = scalePady, ipady=scaleIPady, columnspan=2)
    button1.grid  (row = 2, column = 2, sticky = '', pady = generalPady, padx = generalPadx, columnspan = 2)
    #PWM2:
    pwmLabel2.grid(row = 1, column = 4, sticky = W,  pady = generalPady, padx = generalPadx)
    pwmInput2.grid(row = 1, column = 5, sticky = W,  pady = generalPady)
    pwm2Scale.grid(row = 0, column = 4, sticky = '', pady = scalePady, ipady=scaleIPady, columnspan=2)
    button2.grid  (row = 2, column = 4, sticky = '', pady = generalPady, padx = generalPadx, columnspan = 2)
    #PWM3:
    pwmLabel3.grid(row = 1, column = 6, sticky = W,  pady = generalPady, padx = generalPadx)
    pwmInput3.grid(row = 1, column = 7, sticky = W,  pady = generalPady)
    pwm3Scale.grid(row = 0, column = 6, sticky = '', pady = generalPady, ipady=scaleIPady, columnspan=2)
    button3.grid  (row = 2, column = 6, sticky = '', pady = generalPady, padx = generalPadx, columnspan = 2)
    # Notes for this section: ipady= effectively adjusts the slider size. Increase this 
    # if you need to be more accurate.
    return pwm0, pwm1, pwm2, pwm3

#def changeDutyCycle0(dutyCycle):
#    global pwm0
#    dutyCycle=float(dutyCycle)
#    pwm0.ChangeDutyCycle(dutyCycle)

#def changeDutyCycle1(dutyCycle):
#    global pwm1
#    dutyCycle=float(dutyCycle)
#    pwm1.ChangeDutyCycle(dutyCycle)
#def changeDutyCycle2(dutyCycle):
#    global pwm2
#    dutyCycle=float(dutyCycle)
#    pwm2.ChangeDutyCycle(dutyCycle)

#def changeDutyCycle3(dutyCycle):
#    global pwm3
#    dutyCycle=float(dutyCycle)
#    pwm3.ChangeDutyCycle(dutyCycle)

def readPinSetup():
#Responsible for reading in the settings such as pins and pwm frequencies
    lines=[]
    pins=[] #Stores the pins as integers
    frequencies=[] #Stores the pin frequencies as integers
    try:
        with open(filename) as f:
            lines=f.read().splitlines()
            print(lines)
            for i in range(0,4):
                #Basic for-loop. Needs to be changed when increasing PWM channels
                pin=lines[i][lines[i].find('=')+1:len(lines[i])] #Extract setting data
                pins.append(int(pin)) #append to list
            for j in range(4,8):
                #Basic for-loop. Change it if additional PWM channels needed
                pinFreq=lines[j][lines[j].find('=')+1:len(lines[j])] #Extract frequency value
                frequencies.append(int(pinFreq)) # Append to list
            return pins, frequencies
        f.close()
    except Exception as e:
        print("Error:"+str(e))
        sys.exit(1)
def main():

    print("Welcome to PWM controller! Please read the README for details.")
    [pwm0,pwm1,pwm2,pwm3] = mainWindowSetup() #Sets up the GUI, returning pin details for shutdown
    mainWindow.mainloop() #enter an event listening loop, opens mainWindow
    return [pwm0,pwm1,pwm2,pwm3]

if __name__ == "__main__":
    pwm = main() #Executes program
    #Cleanup:
    pwm[0].stop()
    pwm[1].stop()
    pwm[2].stop()
    pwm[3].stop()
    GPIO.cleanup()

#Programming notes:
#mainloop() should always be at the end of your code
