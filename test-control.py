'''
**********************************************************************
* Filename    : test-control.py
* Description : test control for servo
* Update      : Lee    2019-02-09    New release
**********************************************************************
'''
import time
import sys
import atexit

sys.path.insert(0, './atoicar')
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM

# PiCar setup:  create a default object, no changes to I2C address or frequency
bw = Raspi_MotorHAT(addr=0x6f).getMotor(3)
atexit.register(bw.run, Raspi_MotorHAT.RELEASE)
fw = PWM(0x6F)
fw.setPWMFreq(60)                     # Set frequency to 60 Hz

bw.run(Raspi_MotorHAT.FORWARD);

SPEED = 50
ANGLE = 90

while True:
    key = input("> ")

    if key == 'q':
        break
    elif key == 'w':
        SPEED = 50
        bw.setSpeed(SPEED)
        bw.run(Raspi_MotorHAT.FORWARD);
    elif key == 'x':
        SPEED = 50
        bw.setSpeed(SPEED)
        bw.run(Raspi_MotorHAT.BACKWARD);
    elif key == 'a':
        ANGLE = 65
        fw.turn(ANGLE)
    elif key == 'd':
        ANGLE = 115
        fw.turn(ANGLE)
    elif key == 's':
        ANGLE = 90
        fw.turn(ANGLE)
    elif key == 'z':
        bw.setSpeed(0)

