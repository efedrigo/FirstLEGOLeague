
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 800
MEDIUM_SPEED = 400
SLOW_SPEED = 100
DISTANCE1 = 630

def mission10(myRobot):

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = -1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase; 

    # --- 1) Fast drive straight 620 mm while moving both accessories to mechanical stop ---
 #   drive.reset()  # zero distance measurement
    drive.use_gyro(True)

    # Start accessories using dc (non-blocking); use duty cycle 50%
    myRobot.accessoryLeft.dc(-accessory_left_sign * 50)
    myRobot.accessoryRight.dc(-accessory_right_sign * 60)

    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)

    # Non-blocking straight move
    drive.arc(-120, 90, then=Stop.HOLD, wait=False) #radius, angle
    # Ensure the drive finished as well (poll distance)
    while not drive.done():
        wait(10)

    drive.straight(150,then=Stop.HOLD, wait=False)
    while not drive.done():
        wait(10)

    myRobot.accessoryLeft.stop()
    myRobot.accessoryLeft.reset_angle(0)
    myRobot.accessoryRight.stop()
    myRobot.accessoryRight.reset_angle(0)

    # Non-blocking straight move
    drive.arc(120, 70, then=Stop.HOLD, wait=False) #radius, angle
    while not drive.done():
        wait(10)


    drive.straight(180,then=Stop.HOLD, wait=False)

    while not drive.done():
        wait(10)

    drive.turn(-10)
    myRobot.accessoryLeft.run_angle(650, accessory_left_sign * 340, wait=True)
 
#    drive.turn(-25)
#    drive.arc(40, -10, then=Stop.HOLD, wait=True) #radius, angle

    print("moving down")
    myRobot.accessoryRight.run_angle(1500,  accessory_right_sign*180, wait=True)
    print(myRobot.accessoryRight.angle())
    print("moving up")
    myRobot.accessoryRight.run_angle(500, -accessory_right_sign*200, wait=True)
    print(myRobot.accessoryRight.angle())

    # --- 6) Slow move straight back 200 mm (blocking) ---
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    drive.arc(500, -65, then=Stop.HOLD, wait=True) #radius, angle


    return
