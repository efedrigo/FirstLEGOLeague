from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath

# 200 no, 250 no, 300 no, 500 no, 450 no, 400?
# Speed levels (mm/s)
FAST_SPEED = 500
MEDIUM_FAST_SPEED=320
MEDIUM_SPEED = 300
SLOW_SPEED = 100
DISTANCE1 = 450
DISTANCE2 = 580.5
def mission12(myRobot):

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1
 
    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase

    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)

    drive.straight(DISTANCE1, then=Stop.BRAKE, wait=True)
    wait(0)
    drive.turn(5, then=Stop.BRAKE, wait=True) 
  
    wait(0.000000001)
    
    drive.straight(10, then=Stop.BRAKE, wait=True)
    wait(10)
    drive.turn(3) 
    drive.straight(20)
    drive.turn(3)
    drive.straight(3)
    drive.turn(3)
    drive.straight(70)
    drive.turn(20, then=Stop.BRAKE, wait=True)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    
    wait(10)
    drive.straight(-DISTANCE2)

    #color sensor = very big problem
    return

