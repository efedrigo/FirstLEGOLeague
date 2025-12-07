from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
import umath
from micropython import mem_info

path=[[250,100],
      [250,475],
      [250,1040],
      ]

#from purePursuit import findLookAheadTarget, followPath        

def resetAccessories(myRobot):
  
  print("start accessories reset")

  myRobot.accessoryRight.run_until_stalled(360*3,duty_limit=40)
  myRobot.accessoryLeft.run_until_stalled(-360*3,duty_limit=30)

  wait(3000)

  while not myRobot.accessoryRight.done() or not myRobot.accessoryLeft.done():
    wait(10)

  myRobot.accessoryRight.reset_angle(0)
  myRobot.accessoryLeft.reset_angle(0)
  print("Accessories reset done")

async def runMission(myRobot,myOdometer):
  robot_speed = 600; # mm/s

  resetAccessories(myRobot)

  # move to target
  print("move")
  myRobot.runStraight(500,900)
  print("turn")
  myRobot.curve(40,100,90)

  mem_info()

  # lower left and right arms
  myRobot.accessoryLeft.run_angle(400,800,wait=True)
  myRobot.accessoryRight.run_angle(400,-190,wait=True)
 
  wait(800/400*1000)
  while not myRobot.accessoryLeft.done():
    wait(10)

  print("left:",myRobot.accessoryLeft.angle())
  print("right:",myRobot.accessoryRight.angle())

def mission3_4(myRobot,myOdometer):
  watch = myOdometer.watch

  print("===== MISSION 3-4 =======")
  watch = myOdometer.watch

  async def odo(robot_pos):
    await myOdometer.run(robot_pos[0],robot_pos[1],robot_pos[2])

  robot_pos = [path[0][0],path[0][1], 90]   # mm, mm, degrees

  async def main():
#    await multitask(odo(robot_pos),runMission(myRobot,myOdometer),race=False)
    await multitask(runMission(myRobot,myOdometer),race=False)

  run_task(main())

