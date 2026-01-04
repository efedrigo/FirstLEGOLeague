from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath

# 200 no, 250 no, 300 no, 500 no, 450 no, 400?
# Speed levels (mm/s)
FAST_SPEED = 500
MEDIUM_FAST_SPEED=400
MEDIUM_SPEED = 300
SLOW_SPEED = 100
DISTANCE1 = 550

def mission956(myRobot):

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase

    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=2 * MEDIUM_SPEED)

    # Non-blocking straight move
    drive.straight(750, then=Stop.BRAKE, wait=True)
    drive.turn(90)
    drive.straight(960, then=Stop.BRAKE, wait=True)
    drive.turn(45)
    drive.settings(straight_speed=200, straight_acceleration=2 * FAST_SPEED)
    drive.straight(300, then=Stop.BRAKE, wait=True)
    drive.straight(-100, then=Stop.BRAKE, wait=True)
    drive.turn(-30)
    drive.straight(600, then=Stop.BRAKE, wait=True)
    drive.turn(60)
    drive.straight(-200, then=Stop.BRAKE, wait=True)



    return

