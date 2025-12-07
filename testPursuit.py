from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
import umath

path1=[[1700,0], 
  [1700,200], 
  [1600,300], 
  [1500,450], 
  [1400,500], 
  [1300,550], 
  [1200,700], 
  [1150,800],
  [1200,800],
  [1250,800],
  [1300,800]
]

path2=[[1300,80],
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

from purePursuit import findLookAheadTarget, followPath        

def testPursuit(myRobot,myOdometer):
  watch = myOdometer.watch

  async def odo(robot_pos):
    await myOdometer.run(robot_pos[0],robot_pos[1],robot_pos[2])

  robot_pos = [1700.0, 0.0, 90]   # mm, mm, degrees
  robot_speed = 200; # mm/s

  async def main1():
    await multitask(odo(robot_pos),followPath(myRobot,myOdometer,path1,robot_speed),race=True)
  async def main2():
    await multitask(odo(robot_pos),followPath(myRobot,myOdometer,path2,robot_speed),race=True)

  run_task(main1())

## operate accessories
  wait(2000)
  myRobot.hub.display.icon(Icon.ARROW_LEFT_UP)
  myRobot.accessoryLeft.reset_angle(0);
  myRobot.accessoryLeft.run_angle(360,360);
  wait(2000)

  run_task(main2())
  

