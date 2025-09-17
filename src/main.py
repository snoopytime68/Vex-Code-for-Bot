# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Jonah Despain and Liam Fryar                                 #
# 	Created:      9/9/2025, 9:59:41 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Create the left Motors and group them under the
# MotorGroup "left_motors".
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
left_motors = MotorGroup(left_motor_a, left_motor_b)
# Create the right Motors and group them under the
# MotorGroup "right_motors".
right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_motors = MotorGroup(right_motor_a, right_motor_b)
# Construct a 4-Motor Drivetrain "drivetrain" with the
# DriveTrain class.
drivetrain = DriveTrain(left_motors, right_motors, 319.19, 295, 40, MM, 1)

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

        while True:
        while not controller_1.buttonB.pressing():
            wait(5, MSEC)
        motor_3.spin(FORWARD)
        wait(5, MSEC)
        while True:
        while not controller_1.buttonA.pressing():
            wait(5, MSEC)
        motor_1.spin(FORWARD, 10, VOLT)
        motor_2.spin(FORWARD, 10, VOLT)
        wait(5, MSEC)

def buttonDown(button_pressed) 
    motor1.temperature() 
    motor2.temperature() 
    motor3.temperature() 
    motor4.temperature() 

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
