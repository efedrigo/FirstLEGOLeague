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
    myRobot.accessoryLeft.dc(-accessory_left_sign * 60)

#    drive.straight(740, then=Stop.BRAKE, wait=True)
#    myRobot.rotateAbs(90)
#    drive.straight(940, then=Stop.HOLD, wait=True)

# first part, originally was 540
    drive.straight(560, then=Stop.BRAKE, wait=True)
    myRobot.accessoryLeft.stop()
    myRobot.accessoryLeft.reset_angle(0)

    drive.arc(200,90,then=Stop.BRAKE)
#    drive.straight(760, then=Stop.BRAKE, wait=True)
#    drive.turn(50, then=Stop.HOLD, wait=True)
    drive.straight(680, then=Stop.BRAKE, wait=True)
    drive.arc(200,45,then=Stop.BRAKE)
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
    myRobot.accessoryLeft.run_target(1500, accessory_left_sign * 150, wait=True)
    myRobot.rotateAbs(90,1)

    drive.straight(-120, then=Stop.BRAKE, wait=True)
#    drive.straight(90, then=Stop.BRAKE, wait=True)
    myRobot.rotateAbs(100,1)
    myRobot.accessoryLeft.run_target(1500, accessory_left_sign * 0, wait=False)
    drive.straight(20, then=Stop.BRAKE, wait=True)
    myRobot.rotateAbs(130,1)
    drive.straight(100, then=Stop.BRAKE, wait=True)
    myRobot.rotateAbs(160,2)

    # drive home
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    drive.straight(470, then=Stop.NONE, wait=True)
    drive.arc(-200, 60,then=Stop.BRAKE, wait=True)

    return


  