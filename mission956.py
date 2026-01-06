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
    drive.use_gyro(False)
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=2 * MEDIUM_SPEED)

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 1:", actual_angle)

    # Non-blocking straight move
    drive.straight(760, then=Stop.BRAKE, wait=True)

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 2:", actual_angle)

    myRobot.rotateAbs(90)

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 3:", actual_angle)
    return
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
#    drive.straight(935, then=Stop.BRAKE, wait=True)
    drive.straight(150, then=Stop.BRAKE, wait=True)

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 4:", actual_angle)


    myRobot.rotateAbs(135)

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 5:", actual_angle)

    return
    # ora siamoo davanti il target

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 3:", actual_angle)

    if actual_angle<130:
        drive.straight(-50, then=Stop.BRAKE, wait=True)        
        myRobot.rotate(130-actual_angle)
        drive.straight(50, then=Stop.BRAKE, wait=True)
    

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 4:", actual_angle)

    return

    drive.settings(straight_speed=250, straight_acceleration=2 * FAST_SPEED)
    drive.straight(300, then=Stop.BRAKE, wait=True)
    drive.straight(-100, then=Stop.BRAKE, wait=True)
    drive.turn(-43)
    drive.straight(520, then=Stop.BRAKE, wait=True)
    drive.turn(45)
    drive.straight(-100, then=Stop.BRAKE, wait=True)
    drive.turn(-20)
    drive.straight(-20, then=Stop.BRAKE, wait=True)



    return

