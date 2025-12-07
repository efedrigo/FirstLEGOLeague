from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from uerrno import ENODEV
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis, Icon

hub = InventorHub(front_side=-Axis.X,top_side=Axis.Z);

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A,Direction.CLOCKWISE )
right_motor = Motor(Port.B,Direction.COUNTERCLOCKWISE)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=81.6, axle_track=88)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
drive_base.straight(500)

print(hub.imu.heading())

# Turn around clockwise by 180 degrees.
drive_base.turn(90)
print(hub.imu.heading())
