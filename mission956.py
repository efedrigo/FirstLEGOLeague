from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Icon
from pybricks.tools import wait
import umath as umath

# 200 no, 250 no, 300 no, 500 no, 450 no, 400?
# Speed levels (mm/s)
FAST_SPEED = 500
MEDIUM_FAST_SPEED=400
MEDIUM_SPEED = 300
SLOW_SPEED = 200
DISTANCE1 = 550

def mission956(myRobot):

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase

    drive.reset()  # zero distance measurement
    drive.use_gyro(True)

    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)

#    drive.straight(740, then=Stop.BRAKE, wait=True)
#    myRobot.rotateAbs(90)
#    drive.straight(940, then=Stop.HOLD, wait=True)

    drive.straight(540, then=Stop.BRAKE, wait=True)
    drive.arc(200,90,then=Stop.BRAKE)
    drive.straight(760, then=Stop.BRAKE, wait=True)

    drive.turn(50, then=Stop.HOLD, wait=True)
    wait(100)

    myRobot.rotateAbs(130,0)

    # ora siamo davanti il target

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 3:", actual_angle)

    if actual_angle<120:
        print("** correzione 1")
        myRobot.hub.display.char("!")
        drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * SLOW_SPEED)
        drive.straight(-50, then=Stop.HOLD, wait=True)        
        myRobot.rotateAbs(125)
        drive.straight(50, then=Stop.HOLD, wait=True)
        myRobot.hub.display.icon(Icon.HAPPY)


    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 4:", actual_angle)

    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=2 * MEDIUM_FAST_SPEED)
    drive.straight(480, then=Stop.BRAKE, wait=True)
    drive.straight(-90, then=Stop.BRAKE, wait=True)
    myRobot.rotateAbs(85)

# up to here the position should be reproduceable

# attack 
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=2 * MEDIUM_FAST_SPEED)
    drive.straight(380, then=Stop.BRAKE, wait=True)
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * SLOW_SPEED)
    drive.straight(40, then=Stop.BRAKE, wait=True)
    # impact ores
    myRobot.rotateAbs(45,0)
    drive.straight(-20, then=Stop.BRAKE, wait=True)

    # drive home
    myRobot.rotateAbs(90,0)
    drive.turn(90)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    drive.straight(800, then=Stop.BRAKE, wait=True)


    return
    myRobot.rotateAbs(60,0)

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 5:", actual_angle)

    if (actual_angle>70):
        drive.straight(-40, then=Stop.BRAKE, wait=True)
        drive.turn(20)
        myRobot.rotateAbs(60,1)
        drive.straight(40, then=Stop.BRAKE, wait=True)
        myRobot.hub.display.icon(Icon.HAPPY)

    actual_angle=myRobot.hub.imu.heading();   
    print("actual angle 6:", actual_angle)
    drive.straight(80, then=Stop.BRAKE, wait=True)
    drive.straight(-40, then=Stop.BRAKE, wait=True)

    myRobot.rotateAbs(100)
    myRobot.rotateAbs(45)
    drive.straight(-90, then=Stop.BRAKE, wait=True)

    # final run
    myRobot.rotateAbs(95)
    drive.straight(600, then=Stop.BRAKE, wait=True)
    drive.straight(-300, then=Stop.BRAKE, wait=True)
    myRobot.rotateAbs(160,0)

    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    drive.straight(800, then=Stop.BRAKE, wait=True)

    return

