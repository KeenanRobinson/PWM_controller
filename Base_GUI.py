#*******************************************************************
#                           DESCRIPTION                 
# The following code is a base GUI to allow users to control the     
# duty cycle of PWM signals. It has been tested and works on Python   
# 3.8.7 and 3.x.x 
#                   
# Date created: 01/05/2021         
# Created by: Keenan Robinson       
# ******************************************************************                   

#!usr/bin/env python
from Tkinter import *
#************************************
#       VARIABLE DEFINTIONS         *
        
mainWindow = Tk() # Creates the root window object
mainWindow.title("PWM Controller")
mainWindow.geometry("765x300+10+20") #width x height + XPOS + YPOS

#   END OF VAR. DEFINITIONS         *
#************************************
def mainWindowSetup(): # Sets up the main window with widgets
    #Duty cycle values to update widgets
    dutyCycle0 = IntVar()
    dutyCycle1 = IntVar()
    dutyCycle2 = IntVar()
    dutyCycle3 = IntVar()

    #Create label widgets
    pwmLabel0 = Label(mainWindow, text="PWM0")
    pwmLabel1 = Label(mainWindow, text="PWM1")
    pwmLabel2 = Label(mainWindow, text="PWM2")
    pwmLabel3 = Label(mainWindow, text="PWM3")

    #Create entry widgets
    var = IntVar()
    pwmInput0 = Entry(mainWindow, textvariable=dutyCycle0)
    pwmInput1 = Entry(mainWindow, textvariable=dutyCycle1)
    pwmInput2 = Entry(mainWindow, textvariable=dutyCycle2)
    pwmInput3 = Entry(mainWindow, textvariable=dutyCycle3)

    #Create scale (sliders)
    pwm0Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle0, orient='vertical')
    pwm1Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle1, orient='vertical')
    pwm2Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle2, orient='vertical')
    pwm3Scale = Scale(mainWindow, from_=100, to=0, variable=dutyCycle3, orient='vertical')

    #Grid geometry handler to layout the GUI
    #PWM0:
    pwmLabel0.grid(row = 1, column = 0, sticky = W, pady = 2, padx = 10)
    pwmInput0.grid(row = 1, column = 1, sticky = W, pady = 2)
    pwm0Scale.grid(row=0, column=0, sticky = W, pady=10, ipady=30, columnspan=2)
    #PWM1:
    pwmLabel1.grid(row = 1, column = 2, sticky = W, pady = 2, padx = 10)
    pwmInput1.grid(row = 1, column = 3, sticky = W, pady = 2)
    pwm1Scale.grid(row=0, column=2, sticky = W, pady=10, ipady=30, columnspan=2)
    #PWM2:
    pwmLabel2.grid(row = 1, column = 4, sticky = W, pady = 2, padx = 10)
    pwmInput2.grid(row = 1, column = 5, sticky = W, pady = 2)
    pwm2Scale.grid(row=0, column=4, sticky = W, pady=10, ipady=30, columnspan=2)
    #PWM3:
    pwmLabel3.grid(row = 1, column = 6, sticky = W, pady = 2, padx = 10)
    pwmInput3.grid(row = 1, column = 7, sticky = W, pady = 2)
    pwm3Scale.grid(row=0, column=6, sticky = W, pady=10, ipady=30, columnspan=2)

    # Notes for this section: ipady= effectively adjusts the slider size. Increase this 
    # if you need to be more accurate.

def main():

    print("Welcome to PWM controller! Please read the README for details.")
    mainWindowSetup()
    mainWindow.mainloop() #enter an event listening loop, opens mainWindow
    return 0

if __name__ == "__main__":
    main()

#Programming notes:
#mainloop() should always be at the end of your code
