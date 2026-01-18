# --- START ---
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
DISTANCE1 = 475
DISTANCE2 = 100

def mission12(myRobot):

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1
 
    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase

    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=2 * MEDIUM_FAST_SPEED,turn_rate=150, turn_acceleration=200)
    drive.straight(DISTANCE1, then=Stop.BRAKE, wait=True)
    drive.straight(-10, then=Stop.BRAKE, wait=True)
    myRobot.rotateAbs(0)
  
 #   wait(0.000000001)
    
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * SLOW_SPEED)
    i=0
    while i<3:
        print("i:", i)
        drive.drive(MEDIUM_SPEED,0) # speed,turn rate
        wait(300)
#        drive.straight(40, then=Stop.BRAKE, wait=True)
#        drive.turn(5, then=Stop.BRAKE, wait=True) 
        i+=1 
    drive.straight(-DISTANCE2)
    myRobot.rotateAbs(0)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    drive.straight(-(DISTANCE1+DISTANCE2))
    return
                    
