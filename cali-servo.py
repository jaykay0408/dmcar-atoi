'''
**********************************************************************
* Filename    : cali-servo.py
* Description : calibrate a servo motor
* Update      : Lee    2021-09-30    New release
**********************************************************************
'''

import time
import sys
import atexit

sys.path.insert(0, './atoicar')
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM

# PiCar setup:  create a default object, no changes to I2C address or frequency
fw = PWM(0x6F)
fw.setPWMFreq(60)                     # Set frequency to 60 Hz

# ============== Calibrate Servo for 90 degree =============
# Straight
print("Servo is on 90 degree... Put a servo arm into a servo as 90 degree")
ANGLE = 90
fw.turn(ANGLE)
time.sleep(10)
