from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
import umath

path=[[1650,95],
      [1650,225],
      [1625,270],
      [1575,310],
      [1550,360],
      [1500,450],
      [1450,500],
      [1440,520]
      ]

from purePursuit import findLookAheadTarget, followPath        

def resetAccessories(myRobot):
  print("start motor 1")
  myRobot.accessoryRight.run_until_stalled(1000,duty_limit=40)
  print("done motor 1 - start motor 2")
  myRobot.accessoryLeft.run_until_stalled(1000,duty_limit=40)
  print("done motor 2")

async def run2(myRobot,robot_speed):
  dist = int(-200/myRobot.wheelC*360)
  myRobot.motorLeft.run_angle(robot_speed,dist,wait=False)
  await myRobot.motorRight.run_angle(robot_speed,dist)
  print("done")

def mission9(myRobot,myOdometer):
  watch = myOdometer.watch

  async def odo(robot_pos):
    await myOdometer.run(robot_pos[0],robot_pos[1],robot_pos[2])

  robot_pos = [1650.0, 95.0, 90]   # mm, mm, degrees
  robot_speed = 900; # mm/s

  async def main0():
    myRobot.accessoryRight.reset_angle(0)
    myRobot.accessoryRight.run_angle(600,-360*4)

  async def main1():
    await multitask(odo(robot_pos),followPath(myRobot,myOdometer,path,robot_speed),race=True)

  async def main2():
    await multitask(odo(robot_pos),run2(myRobot,robot_speed/3),race=True)

  resetAccessories(myRobot)

  run_task(main0())
#  run_task(main1())
#  run_task(main2())


