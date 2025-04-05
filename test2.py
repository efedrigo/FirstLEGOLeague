from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
from show import show

print("starting")
hub = InventorHub(front_side=-Axis.X)
run_task(show(hub,9))
print("finished")


