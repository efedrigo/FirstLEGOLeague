from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

colorSensor = ColorSensor(Port.E)
color = colorSensor.color(True)
print(color)
hsv = colorSensor.hsv(True)
print(hsv)
reflectance = colorSensor.reflection()
print(reflectance)
colorSensor.lights.off()
