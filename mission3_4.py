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


#    # Start from a known state for accessories.
#    left_acc.reset_angle(0)
#    right_acc.reset_angle(0)

    # ----------------------------------------------------------------------
    # 1) Straight 900 mm at 500 mm/s
    #    While driving: move both accessories until mechanical stop, then reset.
    # ----------------------------------------------------------------------
    drive.stop()
    drive.settings(500, 500, 180, 180)  # straight_speed, straight_accel, turn_rate, turn_accel

    # Non-blocking straight.

#   these are blocking
#    myRobot.accessoryRight.run_until_stalled(360*3,duty_limit=40)
#    myRobot.accessoryLeft.run_until_stalled(-360*3,duty_limit=30)

    print("start driving")
    drive.straight(840, then=Stop.HOLD, wait=False)

#    # Run accessories until stall (mechanical stop).
    print("start motor right")
    accessoryRight.dc(40)
    print("start motor left")
    accessoryLeft.dc(-50)

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
    drive.arc(60, 90, then=Stop.HOLD, wait=False)

    wait(300)
    # Lower accessories in parallel to the arc.
    accessoryLeft.run_target(500, 460, then=Stop.HOLD, wait=False)
    accessoryRight.run_target(500, -120, then=Stop.HOLD, wait=False)

    # Wait until both the arc and the accessory motions are done.
    while (not drive.done() or
           not (accessoryLeft.done() and accessoryRight.done())):
        wait(10)

    # ----------------------------------------------------------------------
    # 3) Straight 50 mm at 100 mm/s.
    # ----------------------------------------------------------------------
    drive.settings(80, 100, 90, 90)
#    drive.use_gyro(False)
    drive.straight(150, then=Stop.HOLD, wait=True)
#    drive.use_gyro(True)

#    while not drive.done():
#        wait(10)

    # ----------------------------------------------------------------------
    # 4) Raise left accessory to 750° and right accessory back to 0°.
    # ----------------------------------------------------------------------
    accessoryLeft.run_target(200, 400, then=Stop.HOLD, wait=False)
    accessoryRight.run_target(200, -20, then=Stop.HOLD, wait=False)

    while not (accessoryLeft.done() and accessoryRight.done()):
        wait(10)

    # ----------------------------------------------------------------------
    # 5) Move straight BACK 50 mm at 100 mm/s.
    # ----------------------------------------------------------------------
    drive.straight(-170, then=Stop.HOLD, wait=True)

#    while not drive.done():
#        wait(10)

    # ----------------------------------------------------------------------
    # 6) Another arc of 90° to the RIGHT (radius 40 mm, 50 mm/s).
    # ----------------------------------------------------------------------
    drive.settings(300, 300, 300, 300)
    accessoryLeft.run_target(300, 80, then=Stop.HOLD, wait=False)
    drive.turn(95, then=Stop.HOLD, wait=True)

 #   while not drive.done():
  #      wait(10)

    # ----------------------------------------------------------------------
    # 7) Fast straight 900 mm to go back towards the initial position
    #    at 500 mm/s.
    # ----------------------------------------------------------------------
    drive.settings(500, 500, 180, 180)
    drive.straight(800, then=Stop.HOLD, wait=True)

#    while not drive.done():
#        wait(10)

    # Final stop to fully deactivate the drive base.
    drive.stop()

