from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Icon
from pybricks.tools import wait
import umath as umath


def mission14(myRobot):

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase

    drive.reset()  # zero distance measurement
    drive.use_gyro(True)

    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)

    drive.straight(500, then=Stop.BRAKE, wait=True)

    # optionally, raise acessory
    drive.straight(-200, then=Stop.BRAKE, wait=True)

    drive.turn(-90, then=Stop.HOLD, wait=True)

    drive.straight(500, then=Stop.BRAKE, wait=True)
    # optionally, lower acessory


    return