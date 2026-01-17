from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis, Icon
from pybricks.robotics import DriveBase
from pybricks.iodevices import PUPDevice
from pybricks.tools import wait
from uerrno import ENODEV
import umath

def mission3_4(myRobot):
    """
    myRobot must provide:
        - motorLeft       : left drive motor
        - motorRight      : right drive motor
        - driveBase       : pybricks.robotics.DriveBase (new API with arc/straight non-blocking)
        - accessoryLeft   : left accessory motor
        - accessoryRight  : right accessory motor
    """

    wheelD = myRobot.wheelDiameter # diameter, mm
    wheelC = wheelD * umath.pi; #mm 
    D = myRobot.axle; #mm

    motorLeft = myRobot.motorLeft; #Motor(Port.A,positive_direction=Direction.CLOCKWISE);
    motorRight = myRobot.motorRight; #Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE);
    accessoryLeft = myRobot.accessoryLeft; #Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE);
    accessoryRight = myRobot.accessoryRight; #Motor(Port.D,positive_direction=Direction.CLOCKWISE);
    drive = myRobot.driveBase; #DriveBase(motorLeft, motorRight, wheel_diameter=wheelD, axle_track=D)
    drive.use_gyro(True)
    drive.reset(0,0)

    accessoryLeft_sign =1;
    accessoryRight_sign =1;

    # ----------------------------------------------------------------------
    # 1) Straight 900 mm at 500 mm/s
    #    While driving: move both accessories until mechanical stop, then reset.
    # ----------------------------------------------------------------------
    drive.settings(500, 500, 180, 180)  # straight_speed, straight_accel, turn_rate, turn_accel


    print("start driving")
    drive.straight(840, then=Stop.HOLD, wait=False)

#    # Run accessories until stall (mechanical stop).
    print("start motor right")
    accessoryRight.dc(accessoryLeft_sign*50)
    print("start motor left")
    accessoryLeft.dc(accessoryLeft_sign*50)

    left_stalled = False
    right_stalled = False
    reset_done = False

    while not drive.done() or not reset_done:

        # Stall detection for accessories
        if not left_stalled and accessoryLeft.stalled():
            accessoryLeft.stop()
            left_stalled = True
            accessoryLeft.reset_angle(0)
            print("left stalled")

        if not right_stalled and accessoryRight.stalled():
            accessoryRight.stop()
            right_stalled = True
            accessoryRight.reset_angle(0)
            print("right stalled")

        # Once both have stalled, reset their angle exactly once.
        if left_stalled and right_stalled and not reset_done:
            reset_done = True
            print("reset accessories complete")

        if drive.done():
            drive.stop()

        wait(10)

    print("first motion done")
    # Ensure accessories are not running anymore.
    accessoryLeft.stop()
    accessoryRight.stop()

    # ----------------------------------------------------------------------
    # 2) Arc 90° to the RIGHT at 50 mm/s, radius 40 mm (non-blocking arc()).
    #    While driving the arc and before the next motion:
    #       - left accessory -> 800°
    #       - right accessory -> 190°
    # ----------------------------------------------------------------------
    drive.settings(200, 100, 200, 100)

    # Positive angle = right turn in the current DriveBase API.
    drive.arc(70, 90, then=Stop.HOLD, wait=True)

    accessoryLeft.run_target(500, accessoryLeft_sign*(-250), then=Stop.HOLD, wait=False)

#    # Wait until both the arc and the accessory motions are done.
#    while (not drive.done() or
#           not (accessoryLeft.done())):
#        wait(10)

    myRobot.rotateAbs(90)
    accessoryRight.run_target(500, -120, then=Stop.HOLD, wait=True)

    # ----------------------------------------------------------------------
    # 3) move slowly towards target
    # ----------------------------------------------------------------------
    drive.settings(80, 100, 90, 90)

    # get object
    drive.straight(130, then=Stop.HOLD, wait=True)
    accessoryLeft.run_target(500, accessoryLeft_sign*(-260), then=Stop.HOLD, wait=False)
    drive.straight(60, then=Stop.HOLD, wait=True)

    # raise sliglhtly
    drive.settings(100, 100, 200, 100)
    accessoryLeft.run_target(500, accessoryLeft_sign*(-250), then=Stop.HOLD, wait=False)
    #m re-align
    myRobot.rotateAbs(95)
    # raise Indiana Jones
    accessoryRight.run_target(180, -50, then=Stop.HOLD, wait=True)
    wait(2000)
    accessoryRight.run_target(100, -120, then=Stop.HOLD, wait=True)

    # exit backwards
    drive.settings(100, 100, 200, 100)
    drive.straight(-200, then=Stop.HOLD, wait=True)

    myRobot.rotateAbs(130)

    drive.settings(300, 300, 200, 100)
    drive.straight(300, then=Stop.HOLD, wait=True)
    accessoryRight.run_target(100, -135, then=Stop.HOLD, wait=True)
    myRobot.rotateAbs(125)
    drive.settings(100, 100, 200, 100)
    drive.straight(150, then=Stop.HOLD, wait=True)
    drive.turn(-10)

    drive.settings(50, 50, 200, 100)
    accessoryRight.run_target(300, -30, then=Stop.HOLD, wait=False)
    drive.straight(-30, then=Stop.HOLD, wait=True)
    wait(1000)

    # back up
    drive.settings(500, 500, 180, 180)  # straight_speed, straight_accel, turn_rate, turn_accel
    drive.straight(-150, then=Stop.HOLD, wait=True)
    myRobot.rotateAbs(45)

    drive.settings(500, 500, 180, 180)  # straight_speed, straight_accel, turn_rate, turn_accel
    drive.straight(-750, then=Stop.HOLD, wait=True)

    return


