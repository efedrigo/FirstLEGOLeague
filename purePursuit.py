import umath
from pybricks.tools import wait

def _norm2d(dx, dy):
    return umath.sqrt(dx*dx + dy*dy)

def _angle_deg(dy, dx):
    # atan2(y, x) returns radians; convert to degrees
    return umath.atan2(dy, dx) * (180.0 / umath.pi)

def _ang_norm_180(angle_deg):
    # Normalize to [-180, 180)
    angle_deg = (angle_deg + 180.0) % 360.0 - 180.0
    return angle_deg


#
# function
#

def findLookAheadTarget(robot_pos,robot_look_ahead,path):
    sol = []

    rx, ry = float(robot_pos[0]), float(robot_pos[1])
    R = float(robot_look_ahead)

    # Distance to last waypoint (goal)
    gx, gy = float(path[-1][0]), float(path[-1][1])
    dg = _norm2d(gx - rx, gy - ry)
    print("distance to goal:", dg)

    if dg <= R:
        vx, vy = gx - rx, gy - ry
        alpha = _angle_deg(vy, vx)
        d = _norm2d(vx, vy)
        delta_alpha = _ang_norm_180(alpha - float(robot_pos[2]))
        return [gx, gy, d, alpha, delta_alpha]

#
# Parametric line
#
# x(t) = x1+t(x2-x1)
# y(t) = y1+t(y2-y1)
#
# 0 <= t <= 1
#
# t=0 > x(0)=x1, y(0)=y1
# t=1 > x(1)=x2, y(1)=y2
#

    # Iterate over each path segment
    n_path = len(path)
    for n in range(1, n_path):
        x1, y1 = float(path[n - 1][0]), float(path[n - 1][1])
        x2, y2 = float(path[n][0]), float(path[n][1])

        # P = start_point - robot_pos
        Px, Py = x1 - rx, y1 - ry
        # D = end_point - start_point
        Dx, Dy = x2 - x1, y2 - y1

        # Quadratic for circle/segment intersection
        A = Dx*Dx + Dy*Dy
        B = 2.0 * (Dx*Px + Dy*Py)
        C = Px*Px + Py*Py - R*R

        disc = B*B - 4.0*A*C
        # Numerical tolerance to treat "just touching" as tangency
        eps = 1e-12

        if disc > eps:
            sqrt_disc = umath.sqrt(disc)
            for sgn in (1.0, -1.0):
                t = (-B + sgn*sqrt_disc) / (2.0*A)
                if 0.0 <= t <= 1.0:
                    px = x1 + t*Dx
                    py = y1 + t*Dy
                    vx, vy = px - rx, py - ry
                    alpha = _angle_deg(vy, vx)
                    d = _norm2d(vx, vy)
                    delta_alpha = _ang_norm_180(alpha - float(robot_pos[2]))
                    sol.append([px, py, d, alpha, delta_alpha])

        elif abs(disc) <= eps:
            # Tangent case
            t = -B / (2.0*A)
            if 0.0 <= t <= 1.0:
                px = x1 + t*Dx
                py = y1 + t*Dy
                vx, vy = px - rx, py - ry
                alpha = _angle_deg(vy, vx)
                d = _norm2d(vx, vy)
                delta_alpha = _ang_norm_180(alpha - float(robot_pos[2]))
                sol.append([px, py, d, alpha, delta_alpha])

    # Choose the best candidate (smallest |delta_alpha|)
    if len(sol) == 1:
        return sol[0]
    elif len(sol) == 0:
        return []
    else:
        best = sol[0]
        min_yaw = abs(sol[0][4])
        for k in range(1, len(sol)):
            if abs(sol[k][4]) < min_yaw:
                best = sol[k]
                min_yaw = abs(sol[k][4])
        return best

async def followPath(myRobot,myOdometer,path,speed):
    previous_target = []
    robot_speed_initial = speed # mm/s : move it as a parameters
    robot_look_ahead = 1*speed    # mm (initial; updated each step): parameter
    goal_reached_radius = 2.0; # mm

    print("followPath")

    while True:

        robot_pos = myOdometer.getPosition();
        print(robot_pos)

        # Distance to goal
        last_point = path[-1]
        distance_to_goal = _norm2d(last_point[0] - robot_pos[0], last_point[1] - robot_pos[1])
        if distance_to_goal < goal_reached_radius:
            print("End loop with distance:", distance_to_goal)
            break
    
        # Speed: slower near the end
        robot_speed = robot_speed_initial
        if distance_to_goal < robot_speed_initial * 0.9 * 2.0:
            robot_speed = 10.0 + distance_to_goal / 2.0

        # Update look-ahead
        robot_look_ahead = 25.0 + 0.75 * robot_speed

        # Find look-ahead target
        target = findLookAheadTarget(robot_pos, robot_look_ahead, path)
        if not target:
            target = previous_target
        previous_target = target

        # Controller (only if there is a single target)
        if target:
            Ld = target[2]  # distance to target
            delta_alpha = target[4]
            # Yd = Ld * sin(delta_alpha)
            Yd = Ld * umath.sin(delta_alpha / 180.0 * umath.pi)

            # Pure-pursuit curvature and angular velocity
            k = 2.0 * Yd / (Ld * Ld) if Ld != 0.0 else 0.0

            # speed could be adapted to the curvature k 
            # so that omega is not too high
            omega = k * robot_speed  # rad/s

            # set values for motors
            vL = robot_speed-omega*myRobot.D/2
            vR = robot_speed+omega*myRobot.D/2

            # motor.run wants degrees/s
            # space = angle * circunf
            # vel = space/t = angle/t * circunf
            # vel = v_a * circunf
            # v_a = vel/circunf

            mL = vL / myRobot.wheelC * 360;
            mR = vR / myRobot.wheelC * 360;

            print("Controlling with deg",mL,mR)
            myRobot.motorLeft.run(mL)
            myRobot.motorRight.run(mR)

        else:
            # stop robot, target not reachable
            print("No target, stop")
            break

        await wait(10)

    print("End path follower")
