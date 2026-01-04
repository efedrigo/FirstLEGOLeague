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
DISTANCE1 = 630

def mission10(myRobot):
    """Run mission 1 using `myRobot` components.

    Follows the exact sequence requested. Accessory sign variables allow
    swapping directions without changing calls.
    """

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = -1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase; #DriveBase(
#        myRobot.motorLeft,
#        myRobot.motorRight,
 #       myRobot.wheelDiameter,
 #       myRobot.axle
 #   )

    # --- 1) Fast drive straight 620 mm while moving both accessories to mechanical stop ---
 #   drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)

    # Start accessories using dc (non-blocking); use duty cycle 50%
    myRobot.accessoryLeft.dc(-accessory_left_sign * 40)
    myRobot.accessoryRight.dc(-accessory_right_sign * 50)

    # Non-blocking straight move
    drive.arc(-100, 90, then=Stop.HOLD, wait=False) #radius, angle
    # Ensure the drive finished as well (poll distance)
    while not drive.done():
        wait(10)

    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    drive.straight(220,then=Stop.HOLD, wait=False)
    while not drive.done():
        wait(10)

    # Non-blocking straight move
    drive.arc(100, 90, then=Stop.HOLD, wait=False) #radius, angle
    while not drive.done():
        wait(10)


    drive.straight(150,then=Stop.HOLD, wait=False)

    # Wait until both accessories reach their mechanical stops (stalled())
    left_stalled = False
    right_stalled = False
    while not (left_stalled and right_stalled):
        if not left_stalled and myRobot.accessoryLeft.stalled():
            myRobot.accessoryLeft.stop()
            myRobot.accessoryLeft.reset_angle(0)
            left_stalled = True
        if not right_stalled and myRobot.accessoryRight.stalled():
            myRobot.accessoryRight.stop()
            myRobot.accessoryRight.reset_angle(0)
            right_stalled = True
        wait(10)

    while not drive.done():
        wait(10)

    # stop accessories (safety) and ensure angle zeroed
 #   myRobot.accessoryLeft.stop()
 #   myRobot.accessoryRight.stop()
 #   myRobot.accessoryLeft.reset_angle(0)
 #   myRobot.accessoryRight.reset_angle(0)

    # --- 2) Turn left 90 degrees (blocking) ---
 #   drive.turn(-90)

    # --- 3) Slow move straight (medium speed) 250 mm (blocking) ---
    drive.turn(-10)
    myRobot.accessoryLeft.run_target(550, accessory_left_sign * 800, wait=True)
    drive.turn(-25)
    drive.straight(40)

    # --- 5) Raise left accessory to 0° (blocking) ---
    myRobot.accessoryRight.run_target(1000, accessory_right_sign * 550, wait=True)
    myRobot.accessoryRight.run_target(600, accessory_right_sign * 200, wait=True)

    # --- 6) Slow move straight back 200 mm (blocking) ---
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    angle = drive.angle()
    print("angle1:",angle)
    drive.turn(0-angle)
    print("angle2:",drive.angle())
    drive.straight(-100)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    print("angle3:",drive.angle())
    drive.turn(-60)
    drive.straight(-500)

    # --- 5) Raise left accessory to 0° (blocking) ---
 #   myRobot.accessoryRight.run_target(400, accessory_right_sign * 700, wait=True)
#    drive.turn(60)
  #  drive.straight(50)

    # --- 7) Turn 45° to the right (blocking) ---

    # --- 8) Lower right accessory to 100° (blocking) ---
    #myRobot.accessoryRight.run_target(400, accessory_right_sign * 180, wait=True)

    # --- 9) Move straight 200 mm at medium speed (blocking) ---
    #drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    #drive.straight(200)
    # --- 10) Raise right accessory to 0° (blocking) ---
    #myRobot.accessoryRight.run_target(150, accessory_right_sign * 0, wait=True)

    #drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    #drive.straight(100)


    # --- 11) Move straight back 200 mm at medium speed (blocking) ---
   # drive.straight(-200)

    # --- 12) Turn towards initial heading (assume DriveBase.angle() available) ---
    # If DriveBase provides `angle()` (current heading), use it. Otherwise this step
    # does a best-effort short turn to face initial orientation.
#    try:
#        current_heading = drive.angle()
#        drive.turn(-current_heading+15)
#    except Exception:
        # Fallback: assume net heading after previous ops is +45 degrees left, undo it
   # drive.turn(60)

    # --- 13) Fast move straight to return approximately to the initial position ---
    # We assume returning along original heading back by 620 mm (undo initial forward)
  #  drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
  #  drive.straight(-DISTANCE1)

    # Ensure accessories are stopped at the end
 #   myRobot.accessoryLeft.stop()
#    myRobot.accessoryRight.stop()

    return
