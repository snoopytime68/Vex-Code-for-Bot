#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
# Drive Train
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)

# Intake
motor_5 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
motor_6 = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

# Elevator
motor_7 = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
motor_8 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)

# Malicous
optical_20 = Optical(Ports.PORT5)
controller_1 = Controller(PRIMARY)

# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


# Color to String Helper
def convert_color_to_string(col):
    if col == Color.RED:
        return "red"
    if col == Color.GREEN:
        return "green"
    if col == Color.BLUE:
        return "blue"
    if col == Color.WHITE:
        return "white"
    if col == Color.YELLOW:
        return "yellow"
    if col == Color.ORANGE:
        return "orange"
    if col == Color.PURPLE:
        return "purple"
    if col == Color.CYAN:
        return "cyan"
    if col == Color.BLACK:
        return "black"
    if col == Color.TRANSPARENT:
        return "transparent"
    return ""

def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
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
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
left_motors = MotorGroup(left_motor_a, left_motor_b)
# Create the right Motors and group them under the
# MotorGroup "right_motors".
right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
right_motors = MotorGroup(right_motor_a, right_motor_b)
# Construct a 4-Motor Drivetrain "drivetrain" with the
# DriveTrain class.
drivetrain = DriveTrain(left_motors, right_motors, 319.19, 295, 40, MM, 1)

brain = Brain()

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
        #Intake Control. Spits out.
        while True:
            while controller_1.buttonB.pressing():
                wait(5, MSEC)
                motor_5.spin(REVERSE, 10, VOLT)
                motor_6.spin(FORWARD, 10, VOLT)
                motor_7.spin(FORWARD, 10, VOLT)
                wait(5, MSEC)
        
        #Intake Control. Eats it.
        while True:
            while controller_1.buttonA.pressing():
                wait(5, MSEC)
                # Intake
                motor_5.spin(FORWARD, 10, VOLT)
                motor_6.spin(REVERSE, 10, VOLT)
                motor_7.spin(FORWARD, 10, VOLT)
                # Elevator
                motor_8.spin(FORWARD, 10, VOLT)
                wait(5, MSEC)


def buttonDown(button_pressed):
    motor_1.temperature() 
    motor_2.temperature() 
    motor_3.temperature() 
    motor_4.temperature() 

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
