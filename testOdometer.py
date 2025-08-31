from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from odometer import odometer
from motions import move1
from robot import robot

watch = StopWatch()


myRobot = robot()
myOdometer = odometer(myRobot,watch);

#accessoryLeft.run_angle(50,90) #move at 50 deg/s to 90 deg

robot_pos = [1700.0, 0.0, 90]   # mm, mm, degrees

async def odo(robot_pos):
    await myOdometer.run(robot_pos[0],robot_pos[1],robot_pos[2])

#run_task(odo())
async def main():
#    await multitask(move(),myOdometer.run(),race=True)
    await multitask(move1(myRobot.motorLeft,myRobot.motorRight),odo(robot_pos),race=True)

run_task(main())

pos=myOdometer.getPosition()
print(0,",",pos[0],",",pos[1],",",pos[2],",",pos[3],",",1 if pos[4] else 0)
