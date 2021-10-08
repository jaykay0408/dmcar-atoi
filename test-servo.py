'''
**********************************************************************
* Filename    : test-servo.py
* Description : test for server
* Update      : Lee    2019-02-08    New release
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

# ============== Back wheels =============
# 'forward':

for i in range(40, 100, 10):
    bw.setSpeed(i)
    bw.run(Raspi_MotorHAT.FORWARD);
    time.sleep(2)
	
# 'backward':
for i in range(40, 100, 10):
    bw.setSpeed(i)
    bw.run(Raspi_MotorHAT.BACKWARD);
    time.sleep(2)

# 'stop':
bw.setSpeed(0)
bw.run(Raspi_MotorHAT.RELEASE)

# ============== Front wheels =============
# Turn Left
ANGLE = 65
fw.turn(ANGLE)
time.sleep(1)

# Straight
ANGLE = 90
fw.turn(ANGLE)
time.sleep(1)

# Turn Right
ANGLE = 115
fw.turn(ANGLE)
time.sleep(1)

# Straight
ANGLE = 90
fw.turn(ANGLE)
time.sleep(1)

# Angle 60 degree to 120 degree
for i in range(60, 120, 5):
    print(i)
    fw.turn(i)
    time.sleep(1)

fw.turn(90)
