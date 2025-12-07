# MicroPython script for Pybricks
# Mission 1 for a differential drive robot with two accessories.

from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as math  # Pybricks uses umath instead of math


# Speed levels in mm/s
FAST_SPEED = 600
MEDIUM_SPEED = 300
SLOW_SPEED = 100


def mission1(myRobot):
    """
    myRobot must provide:
        - motorLeft
        - motorRight
        - accessoryLeft
        - accessoryRight
        - axle               (distance between the wheels, in mm)
        - wheelDiameter      (wheel diameter, in mm)
    """

    # -------------------------------------------------------------------------
    # Initialize drive base
    # -------------------------------------------------------------------------
    drive_base = DriveBase(
        myRobot.motorLeft,
        myRobot.motorRight,
        myRobot.wheelDiameter,
        myRobot.axle,
    )

    # Optionally, store drive_base in myRobot for later usage (not required)
    myRobot.drive_base = drive_base

    # Helper angle conversion
    def deg_to_rad(deg):
        return deg * math.pi / 180.0

    # -------------------------------------------------------------------------
    # Pose tracking (x, y in mm; heading in degrees, 0 = initial heading)
    # -------------------------------------------------------------------------
    x = 0.0
    y = 0.0
    heading_deg = 0.0

    def update_straight_pose(x, y, heading_deg, distance):
        """Update pose after a straight move of 'distance' mm."""
        theta = deg_to_rad(heading_deg)
        x_new = x + distance * math.cos(theta)
        y_new = y + distance * math.sin(theta)
        return x_new, y_new

    def update_arc_pose(x, y, heading_deg, radius, angle_deg):
        """
        Update pose after an arc with given radius (mm) and turn angle (deg).
        Positive angle = left turn, negative = right turn.
        """
        theta = deg_to_rad(heading_deg)
        dtheta = deg_to_rad(angle_deg)
        r = radius

        # Center of rotation (circle center of robot path)
        cx = x - r * math.sin(theta)
        cy = y + r * math.cos(theta)

        theta2 = theta + dtheta

        x2 = cx + r * math.sin(theta2)
        y2 = cy - r * math.cos(theta2)
        heading2_deg = heading_deg + angle_deg

        return x2, y2, heading2_deg

    # -------------------------------------------------------------------------
    # 1) Fast drive straight for 400 mm while moving both accessories in parallel
    # -------------------------------------------------------------------------
    drive_base.settings(
        straight_speed=FAST_SPEED,
        straight_acceleration=2 * FAST_SPEED,
    )

    # Reset odometry distance
    drive_base.reset()

    # Start accessories: move towards mechanical stop with dc (non-blocking)
    # NOTE: left accessory must use negative duty cycle.
    myRobot.accessoryLeft.dc(-80)
    myRobot.accessoryRight.dc(-80)

    # Non-blocking straight motion
    drive_base.straight(600, then=Stop.BRAKE, wait=False)

    left_stalled = False
    right_stalled = False
    reset_done = False

    while not drive_base.done() or not reset_done:

        # Stall detection for accessories
        if not left_stalled and myRobot.accessoryLeft.stalled():
            myRobot.accessoryLeft.stop()
            left_stalled = True
            myRobot.accessoryLeft.reset_angle(0)
            print("left stalled")

        if not right_stalled and myRobot.accessoryRight.stalled():
            myRobot.accessoryRight.stop()
            right_stalled = True
            myRobot.accessoryRight.reset_angle(0)
            print("right stalled")

        # Once both have stalled, reset their angle exactly once.
        if left_stalled and right_stalled and not reset_done:
            reset_done = True
            print("reset accessories complete")

        if drive_base.done():
            drive_base.stop()

        wait(10)


    # Wait until the straight motion finishes
    # (poll distance until we reach at least 600 mm)
 #   while drive_base.distance() < 600:
 #       wait(10)

    print("end first drive")
    # Stop accessories and reset their angles after they reached the stop
    myRobot.accessoryLeft.stop()
    myRobot.accessoryRight.stop()
    myRobot.accessoryLeft.reset_angle(0)
    myRobot.accessoryRight.reset_angle(0)

    # Update pose (forward 400 mm)
    x, y = update_straight_pose(x, y, heading_deg, 400.0)

    # -------------------------------------------------------------------------
    # 2) Drive an arc of 45° to the right at the same speed, radius 100 mm
    #    (blocking, no parallel accessory motion)
    # -------------------------------------------------------------------------
    # Right turn = negative angle
    radius = 200.0
    angle_right = 45.0

    drive_base.arc(radius, angle_right)  # blocking
    x, y, heading_deg = update_arc_pose(x, y, heading_deg, radius, angle_right)

    # -------------------------------------------------------------------------
    # 3) Drive an arc of 135° to the left at the same speed, radius 100 mm
    # -------------------------------------------------------------------------
    angle_left = 135.0  # left turn = positive angle
    radius = -200.0

    drive_base.arc(radius, angle_left)  # blocking
    x, y, heading_deg = update_arc_pose(x, y, heading_deg, radius, angle_left)

    # -------------------------------------------------------------------------
    # 4) Slow move straight for 250 mm (blocking)
    # -------------------------------------------------------------------------
    drive_base.settings(
        straight_speed=SLOW_SPEED,
        straight_acceleration=2 * SLOW_SPEED,
    )

    drive_base.straight(250)
    x, y = update_straight_pose(x, y, heading_deg, 250.0)

    # -------------------------------------------------------------------------
    # 5) Lower the left accessory to 100° (blocking, no robot motion)
    # -------------------------------------------------------------------------
    # Start from 0°, move down to +100°
    myRobot.accessoryLeft.run_target(200, 100)  # speed 200 deg/s

    # -------------------------------------------------------------------------
    # 6) Raise the left accessory back to 0° (blocking)
    # -------------------------------------------------------------------------
    myRobot.accessoryLeft.run_target(200, 0)

    # -------------------------------------------------------------------------
    # 7) Slow move straight back for 200 mm (blocking)
    # -------------------------------------------------------------------------
    drive_base.straight(-200)
    x, y = update_straight_pose(x, y, heading_deg, -200.0)

    # -------------------------------------------------------------------------
    # 8) Turn 45° to the right (blocking)
    # -------------------------------------------------------------------------
    drive_base.turn(45)  # right: negative
    heading_deg -= 45.0

    return

    # -------------------------------------------------------------------------
    # 9) Lower the right accessory to -100° (blocking)
    # -------------------------------------------------------------------------
    # Start from 0°, move down to -100°
    myRobot.accessoryRight.run_target(200, -100)

    # -------------------------------------------------------------------------
    # 10) Move straight 200 mm at medium speed (blocking)
    # -------------------------------------------------------------------------
    drive_base.settings(
        straight_speed=MEDIUM_SPEED,
        straight_acceleration=2 * MEDIUM_SPEED,
    )

    drive_base.straight(200)
    x, y = update_straight_pose(x, y, heading_deg, 200.0)

    # -------------------------------------------------------------------------
    # 11) Raise the right accessory back to 0° (blocking)
    # -------------------------------------------------------------------------
    myRobot.accessoryRight.run_target(200, 0)

    # -------------------------------------------------------------------------
    # 12) Move straight back 200 mm at medium speed (blocking)
    # -------------------------------------------------------------------------
    drive_base.straight(-200)
    x, y = update_straight_pose(x, y, heading_deg, -200.0)

    # -------------------------------------------------------------------------
    # 13) Turn in the direction of the initial position (0, 0)
    # -------------------------------------------------------------------------
    # Vector from current position to origin
    dx = -x
    dy = -y

    # Global angle (in radians) from current pose to origin
    target_theta = math.atan2(dy, dx)  # result in radians

    # Convert to degrees
    target_heading_deg = target_theta * 180.0 / math.pi

    # Required turn (difference between target heading and current heading)
    turn_deg = target_heading_deg - heading_deg

    # Normalize angle to [-180, 180] for a shorter turn (optional)
    while turn_deg > 180:
        turn_deg -= 360
    while turn_deg < -180:
        turn_deg += 360

    # Perform the turn (blocking)
    drive_base.turn(turn_deg)
    heading_deg += turn_deg

    # -------------------------------------------------------------------------
    # 14) Fast move straight to return to the initial position (0, 0)
    # -------------------------------------------------------------------------
    # Distance to origin
    dist_to_origin = math.sqrt(dx * dx + dy * dy)

    drive_base.settings(
        straight_speed=FAST_SPEED,
        straight_acceleration=2 * FAST_SPEED,
    )

    drive_base.straight(dist_to_origin)

    # We are now (ideally) back at (0,0) with heading pointing towards origin.
    # If desired, we could re-zero pose:
    # x, y = 0.0, 0.0
    # heading_deg = 0.0
