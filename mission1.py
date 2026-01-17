
"""MicroPython mission script for Pybricks.

Provides `mission1(myRobot)` which runs the sequence requested by the user.

Expect `myRobot` to expose:
 - `motorLeft`, `motorRight` (pybricks Motor objects)
 - `accessoryLeft`, `accessoryRight` (pybricks Motor objects)
 - `axle` (mm)
 - `wheelDiameter` (mm)
 Optionally: `gyro` (a GyroSensor) — if present it will be passed to DriveBase

Notes:
 - Uses `umath` (Pybricks) instead of `math`.
 - Uses non-blocking drive when accessories move in parallel.
 - Uses `dc(...)` (50%) for accessory parallel motion to find mechanical stops.
"""

from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 500
MEDIUM_SPEED = 300
SLOW_SPEED = 100
DISTANCE1 = 650

def mission1(myRobot):
    """Run mission 1 using `myRobot` components.

    Follows the exact sequence requested. Accessory sign variables allow
    swapping directions without changing calls.
    """

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase

    # --- 1) Fast drive straight 620 mm while moving both accessories to mechanical stop ---
    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED,turn_rate=100, turn_acceleration=100)

    # Start accessories using dc (non-blocking); use duty cycle 50%
    myRobot.accessoryLeft.dc(-accessory_left_sign * 60)
    myRobot.accessoryRight.dc(-accessory_right_sign * 50)

    # Non-blocking straight move
    drive.straight(DISTANCE1, then=Stop.BRAKE, wait=False)

    # Wait until both accessories reach their mechanical stops (stalled())
    left_stalled = False
    right_stalled = False
    i=0
    while not (left_stalled and right_stalled) and i<100 :
        if not left_stalled and myRobot.accessoryLeft.stalled():
            myRobot.accessoryLeft.stop()
            myRobot.accessoryLeft.reset_angle(0)
            left_stalled = True
        if not right_stalled and myRobot.accessoryRight.stalled():
            myRobot.accessoryRight.stop()
            myRobot.accessoryRight.reset_angle(0)
            right_stalled = True
        i+=1
        wait(10)

    # Ensure the drive finished as well (poll distance)
    while abs(drive.distance()- DISTANCE1)>5:
        wait(10)

    # stop accessories (safety) and ensure angle zeroed
    myRobot.accessoryLeft.stop()
    myRobot.accessoryRight.stop()
    myRobot.accessoryLeft.reset_angle(0)
    myRobot.accessoryRight.reset_angle(0)

    # --- 2) Turn left 90 degrees (blocking) ---
    myRobot.rotateAbs(-115)
    myRobot.rotateAbs(-65)
    myRobot.rotateAbs(-90)

    # --- 3) Slow move straight (medium speed) 250 mm (blocking) ---
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * SLOW_SPEED)
    drive.straight(102)


    drive.straight(120)
    # on target
    myRobot.accessoryLeft.run_target(1000, accessory_left_sign * 200, wait=True)
    myRobot.accessoryLeft.run_target(1000, accessory_left_sign * 0, wait=True)

    # --- 6) Slow move straight back 200 mm (blocking) ---
    drive.straight(-150)

    # --- 7) Turn 45° to the right (blocking) ---
    myRobot.rotateAbs(-50)

    # get the object
    myRobot.accessoryRight.run_target(110, accessory_right_sign * 105, wait=True)
    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    drive.straight(180)
    myRobot.accessoryRight.run_target(100, accessory_right_sign * 0, wait=False)
    # here I got the object
    drive.straight(-40)

    i=0
    while abs(myRobot.accessoryRight.angle())> abs(accessory_right_sign * 10) and i<100:
        wait(10)
        i+=1

    myRobot.rotateAbs(-37)

    # lower the accessory to push
    myRobot.accessoryLeft.run_target(600, accessory_left_sign * 1000, wait=True)

    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    drive.straight(200)

    myRobot.accessoryLeft.run_target(600, accessory_left_sign * 0, wait=True)
    drive.straight(200)

    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    # --- 11) Move straight back 200 mm at medium speed (blocking) ---
    drive.straight(-200)

    # --- 12) Turn towards initial heading (assume DriveBase.angle() available) ---
    # If DriveBase provides `angle()` (current heading), use it. Otherwise this step
    # does a best-effort short turn to face initial orientation.
#    try:
#        current_heading = drive.angle()
#        drive.turn(-current_heading+15)
#    except Exception:
        # Fallback: assume net heading after previous ops is +45 degrees left, undo it
    myRobot.rotateAbs(-160)

    # --- 13) Fast move straight to return approximately to the initial position ---
    # We assume returning along original heading back by 620 mm (undo initial forward)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    drive.straight(450)

    return
