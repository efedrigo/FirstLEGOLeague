
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

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase; 

    # --- 1) Fast drive straight 620 mm while moving both accessories to mechanical stop ---
 #   drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)

    # Start accessories using dc (non-blocking); use duty cycle 50%
    myRobot.accessoryLeft.dc(-accessory_left_sign * 50)
    myRobot.accessoryRight.dc(-accessory_right_sign * 60)

    # Non-blocking straight move
    drive.arc(-120, 90, then=Stop.HOLD, wait=False) #radius, angle
    # Ensure the drive finished as well (poll distance)
    while not drive.done():
        wait(10)

    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    drive.straight(150,then=Stop.HOLD, wait=False)
    while not drive.done():
        wait(10)

    # Non-blocking straight move
    drive.arc(120, 70, then=Stop.HOLD, wait=False) #radius, angle
    while not drive.done():
        wait(10)


    drive.straight(135,then=Stop.HOLD, wait=False)

    # Wait until both accessories reach their mechanical stops (stalled())
    left_stalled = False
    right_stalled = False
    i=0
    while not (left_stalled and right_stalled) and i<8:
        if not left_stalled and myRobot.accessoryLeft.stalled():
            myRobot.accessoryLeft.stop()
            myRobot.accessoryLeft.reset_angle(0)
            left_stalled = True
        if not right_stalled and myRobot.accessoryRight.stalled():
            myRobot.accessoryRight.stop()
            myRobot.accessoryRight.reset_angle(0)
            right_stalled = True
        wait(10)
        i+=1

    while not drive.done():
        wait(10)

    drive.turn(-10)
    myRobot.accessoryLeft.run_angle(650, accessory_left_sign * 290, wait=True)
 
    drive.turn(-25)
#    drive.arc(40, -10, then=Stop.HOLD, wait=True) #radius, angle

    print("moving down")
    myRobot.accessoryRight.run_angle(1500,  accessory_right_sign*200, wait=True)
    print(myRobot.accessoryRight.angle())
    print("moving up")
    myRobot.accessoryRight.run_angle(1500, -accessory_right_sign*10, wait=True)
    print(myRobot.accessoryRight.angle())
    return

    # --- 6) Slow move straight back 200 mm (blocking) ---
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
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
