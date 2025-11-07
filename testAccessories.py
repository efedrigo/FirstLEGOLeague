from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from uerrno import ENODEV

motorLeft = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE);
motorRight = Motor(Port.B,positive_direction=Direction.CLOCKWISE);

print("moving left")
motorLeft.run_time(100,1000)
wait(1000)
print("moving right")
motorRight.run_time(100,1000)
wait(1000)

accessoryLeft = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE);
accessoryRight = Motor(Port.D,positive_direction=Direction.CLOCKWISE);

print("moving accessory left")
accessoryLeft.run_time(100,1000)
wait(1000)
print("moving accessory right")
accessoryRight.run_time(100,1000)
wait(1000)

print("reading color")
colorSensor = ColorSensor(Port.E)
color = colorSensor.color(True)
print(color)
hsv = colorSensor.hsv(True)
print(hsv)
reflectance = colorSensor.reflection()
print(reflectance)
colorSensor.lights.off()
