#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
# Drive Train
controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

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

# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis2 + axis4
            # right = axis2 - axis4
            drivetrain_left_side_speed = controller_1.axis2.position() + controller_1.axis4.position()
            drivetrain_right_side_speed = controller_1.axis2.position() - controller_1.axis4.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

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
        # Intake Controls
        if controller_1.buttonR2.pressing():
            motor_5.spin(FORWARD, 10, VOLT)
            motor_6.spin(REVERSE, 10, VOLT)
            motor_7.spin(FORWARD, 10, VOLT)
            # Elevator
            motor_8.spin(REVERSE, 10, VOLT)
            motor_9.spin(FORWARD, 10, VOLT)
            pass
        # Outtake Controls
        elif controller_1.buttonR1.pressing():
            motor_5.spin(REVERSE, 10, VOLT)
            motor_6.spin(FORWARD, 10, VOLT)
            motor_7.spin(REVERSE, 10, VOLT)
            # Elevator 
            motor_8.spin(REVERSE, 10, VOLT)
            motor_9.spin(FORWARD, 10, VOLT)
            pass
        # Stops motors if button R1 or R2 is not being pressed
        else:
            motor_5.stop()                
            motor_6.stop()                
            motor_7.stop()   
            #Elevator
            motor_8.stop()
            motor_9.stop()            
            pass
#scoring output
        if controller_1.buttonLeft.pressed():
        
            if controller_1.buttonL2.pressing():
                motor_10.spin(FORWARD, 10, VOLT)
                pass

            else:
                motor_10.stop()
                pass
        elif controller_1.buttonRight.pressed():
        
        else:



            #Debug 
        if controller_1.buttonUp.pressing():
            motor_1.temperature() 
            motor_2.temperature() 
            motor_3.temperature() 
            motor_4.temperature()
            motor_5.temperature() 
            motor_6.temperature() 
            motor_7.temperature() 
            motor_8.temperature()
            motor_9.temperature() 
            motor_10.temperature()
            pass
            





# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
