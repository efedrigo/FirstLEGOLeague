
"""MicroPython mission script for Pybricks.

Provides `mission8(myRobot)` which runs the sequence requested by the user.

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
#####START
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 500
MEDIUM_FAST_SPEED = 400
MEDIUM_SPEED = 300
SLOW_SPEED = 100
DISTANCE1 = 380

def mission8(myRobot):
    """Run mission 8 using `myRobot` components.

    Follows the exact sequence requested. Accessory sign variables allow
    swapping directions without changing calls.
    """
    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = -1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase
   
    # --- 1) vai avanti e dai delle martellate ---
    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=FAST_SPEED)

    # setta la posizione di partenza di ogni attachment
    myRobot.accessoryLeft.reset_angle(0)
    myRobot.accessoryRight.reset_angle(0)

    drive.straight(DISTANCE1, then=Stop.BRAKE, wait=True)

    """
    Per muoveere il martello, un ingranaggio piccolo (sul motore) è collegato ad uno grande (sull'attachment).
    L'ingranaggio piccolo ha 12 denti, il grande 20: per dare una martellata, il motore deve fare 20/12=5/3 giri.
    Non posso usare run_target() per portare il martello ad una posizione fissa, perchè ad una certa posizione del 
    motore non corrisponde sempre la stessa posizione fissa del martello (cambia dopo ogni giro).
    """
    mart_num =   4    * 20/12*360 # il primo numero è il numero di martellate 
    mart_speed = 1.5  * 20/12*360 # il primo numero è il numero di martellate al secondo
    myRobot.accessoryRight.run_angle(mart_speed, mart_num, then=Stop.HOLD, wait=True)

    myRobot.accessoryRight.stop()
    

# --- 2) Gira a destra e spingi la leva
    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=FAST_SPEED)

    drive.turn(-90)
    drive.straight(148, then=Stop.BRAKE, wait=True)
    drive.turn(-50)
    drive.straight(100, then=Stop.BRAKE, wait=True)

# --- 3) Torna alla base
    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=FAST_SPEED)

    drive.turn(-68) # da testare
    drive.straight(300, then=Stop.BRAKE, wait=True)

#   wait(n. seconds*1 second (=1000 milliseconds))
    wait(4*1000)

# --- 4) Vai ad alzare il tesoro
    drive.reset()
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_FAST_SPEED, straight_acceleration=FAST_SPEED)

    drive.turn(-20)
    drive.straight(100, then=Stop.BRAKE, wait=True)
    
    
# --- 5) Torna alla base e finisci alla missione Forza Italia :)

    drive.straight(-100, then=Stop.BRAKE, wait=True)
    print("M Trump, W Mattarella :)")


    return




    # Wait until both accessories reach their mechanical stops (stalled())
    #left_stalled = False
    #right_stalled = False
    #while not (left_stalled and right_stalled):
    #    if not left_stalled and myRobot.accessoryLeft.stalled():
    #        myRobot.accessoryLeft.stop()
    #        myRobot.accessoryLeft.reset_angle(0)
    #        left_stalled = True
    #    if not right_stalled and myRobot.accessoryRight.stalled():
    #        myRobot.accessoryRight.stop()
    #        myRobot.accessoryRight.reset_angle(0)
    #        right_stalled = True
    #    wait(10)

    return
    # Ensure the drive finished as well (poll distance)
    while abs(drive.distance()) < DISTANCE1:
        wait(10)

    # stop accessories (safety) and ensure angle zeroed
    myRobot.accessoryLeft.stop()
    myRobot.accessoryRight.stop()
    myRobot.accessoryLeft.reset_angle(0)
    myRobot.accessoryRight.reset_angle(0)

    # --- 2) Turn left 90 degrees (blocking) ---
    drive.turn(-90)

    # --- 3) Slow move straight (medium speed) 250 mm (blocking) ---
    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    drive.straight(220)

    # --- 4) Lower left accessory to 100° (blocking, no robot motion) ---
    # run_target(speed_deg_per_s, angle_deg)
    myRobot.accessoryLeft.run_target(600, accessory_left_sign * 800, wait=True)

    # --- 5) Raise left accessory to 0° (blocking) ---
    myRobot.accessoryLeft.run_target(600, accessory_left_sign * 0, wait=True)

    # --- 6) Slow move straight back 200 mm (blocking) ---
    drive.straight(-150)

    # --- 7) Turn 45° to the right (blocking) ---
    drive.turn(45)

    # --- 8) Lower right accessory to 100° (blocking) ---
    myRobot.accessoryRight.run_target(400, accessory_right_sign * 180, wait=True)

    # --- 9) Move straight 200 mm at medium speed (blocking) ---
    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    drive.straight(200)
    # --- 10) Raise right accessory to 0° (blocking) ---
    myRobot.accessoryRight.run_target(150, accessory_right_sign * 0, wait=True)

    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=2 * MEDIUM_SPEED)
    drive.straight(100)


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
    drive.turn(60)

    # --- 13) Fast move straight to return approximately to the initial position ---
    # We assume returning along original heading back by 620 mm (undo initial forward)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=2 * FAST_SPEED)
    drive.straight(-DISTANCE1)

    # Ensure accessories are stopped at the end
    myRobot.accessoryLeft.stop()
    myRobot.accessoryRight.stop()


    return
