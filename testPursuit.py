from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
import umath

path=[[1700,0], 
  [1700,200], 
  [1600,300], 
  [1500,450], 
  [1400,500], 
  [1300,550], 
  [1200,700], 
  [1150,800], 
  [950,800],
  [900,800],
  [800,700],
  [700,600],
  [600,500],
  [500,400],
  [400,400],
  [300,500],
  [200,600],
  [100,600],
  [50,600]
]

from odometer import odometer
from purePursuit import findLookAheadTarget, followPath        
from robot import robot

watch = StopWatch()

#
# robot def
#


myRobot = robot()

myOdometer = odometer(myRobot,watch);

async def odo(robot_pos):
    await myOdometer.run(robot_pos[0],robot_pos[1],robot_pos[2])

robot_pos = [1700.0, 0.0, 90]   # mm, mm, degrees
robot_speed = 200; # mm/s

async def main():
    await multitask(odo(robot_pos),followPath(myRobot,myOdometer,path,robot_speed),race=True)

run_task(main())


