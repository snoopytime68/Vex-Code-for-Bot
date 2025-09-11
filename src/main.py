# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Jonah and Liam                                                    #
# 	Created:      9/9/2025, 9:59:41 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
optic = optic(ports.port1)
color = optical.color(blue)
controller = controller()

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        wait(20, MSEC)

def buttonDown(button_pressed) 
    motor1.temperature(units) 
    motor2.temperature(units) 
    motor3.temperature(units) 
    motor4.temperature(units) 
# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()