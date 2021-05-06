#*******************************************************************
#                           DESCRIPTION                 
# The following code is a base GUI to allow users to control the     
# duty cycle of 4 PWM pins on the Beaglebone (Black). 
# It still needs to be tested. 
#
# Please read the README for details on its operation. Settings are
# configured in a text file.
#
# Date created: 06/05/2021
# Created by: Keenan Robinson
# ******************************************************************                   

from Tkinter import *
import sys
import Adafruit_BBIO.PWM as PWM #BB setting

#************************************
#       VARIABLE DEFINTIONS         *

mainWindow = Tk() # Creates the root window object
mainWindow.title("Beaglebone PWM Controller")
mainWindow.geometry("640x250+20+20") #width x height + XPOS + YPOS
filename= "pinSetup_BB.txt" #File for configuration settings

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

    #BB Settings: Configure pins
    pins, pinFrequency = readPinSetup()
    #PWM.start("pin", duty cycle, frequency, polarity)
    #Example pin: P9_14, "pin" = "P9_14"
    #Default: PWM.start("pin", 50, 1000, 1)
    PWM.start(pins[0], 0, pinFrequency[0], 1)
    PWM.start(pins[1], 0, pinFrequency[1], 1)
    PWM.start(pins[2], 0, pinFrequency[2], 1)
    PWM.start(pins[3], 0, pinFrequency[3], 1)
    #BB settings end

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
    button0 = Button(mainWindow,text="Set Duty Cycle [0]",command=lambda: PWM.set_duty_cyle(pins[0], dutyCycle0.get()))
    button1 = Button(mainWindow,text="Set Duty Cycle [1]",command=lambda: PWM.set_duty_cyle(pins[1], dutyCycle1.get()))
    button2 = Button(mainWindow,text="Set Duty Cycle [2]",command=lambda: PWM.set_duty_cyle(pins[2], dutyCycle2.get()))
    button3 = Button(mainWindow,text="Set Duty Cycle [3]",command=lambda: PWM.set_duty_cyle(pins[3], dutyCycle3.get()))

    #Create scale (sliders)
    pwm0Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle0, orient='vertical', command=lambda x: PWM.set_duty_cyle(pins[0], dutyCycle0.get()))
    pwm1Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle1, orient='vertical', command=lambda x: PWM.set_duty_cyle(pins[1], dutyCycle1.get()))
    pwm2Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle2, orient='vertical', command=lambda x: PWM.set_duty_cyle(pins[2], dutyCycle2.get()))
    pwm3Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle3, orient='vertical', command=lambda x: PWM.set_duty_cyle(pins[3], dutyCycle3.get()))

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
    return pins #return these for cleanup later

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
                pins.append(pin) #append to list
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
    pins = mainWindowSetup() #Sets up the GUI, returning pin details for shutdown
    mainWindow.mainloop() #enter an event listening loop, opens mainWindow
    return pins #return these for cleanup later

if __name__ == "__main__":
    pwm = main() #Executes program
    #Cleanup:
    PWM.stop(pwm[0])
    PWM.stop(pwm[1])
    PWM.stop(pwm[2])
    PWM.stop(pwm[3])
    PWM.cleanup()

#Programming notes:
#mainloop() should always be at the end of your code