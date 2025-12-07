from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
import umath

path=[[255,0],
      [380, 500],
      [380, 650],
      [340, 640],
      [220, 640],
      [210, 640]      
      ]

from purePursuit import findLookAheadTarget, followPath        

async def moveForward(myRobot,speed,distance):
  dist = int(distance/myRobot.wheelC*360)
  myRobot.motorLeft.run_angle(speed,dist,wait=False)
  await myRobot.motorRight.run_angle(speed,dist)
  print("done vmoce forward")

async def resetAccessories(myRobot):
  
  myRobot.accessoryRight.run_until_stalled(-360*2,duty_limit=30)
  myRobot.accessoryLeft.run_until_stalled(-360*2,duty_limit=30)

  while not myRobot.accessoryRight.done() or not myRobot.accessoryLeft.done():
    wait(10)

  myRobot.accessoryRight.reset_angle(0)
  myRobot.accessoryLeft.reset_angle(0)

  print("Accessories reset")

async def runMission(myRobot,myOdometer):
  robot_speed = 400; # mm/s
  print("resetting accessories")
  # reset accessories
  await resetAccessories(myRobot)
 
  # get to first target
  await followPath(myRobot,myOdometer,path,robot_speed)
  print("target reached")

  # move forward 3cm
  await moveForward(myRobot,200,30)

  # operate accessory left
  print("left down")
  await myRobot.accessoryLeft.run_angle(500,700)

  wait(1000)

  print("left up")
  await myRobot.accessoryLeft.run_target(500,0)
  # move back
  await moveForward(myRobot,200,-100)

  # lower right arm
  print("right down")
  await myRobot.accessoryRight.run_angle(500,250)
  print("angle:",myRobot.accessoryRight.angle())
  # go to second target

  wait(1000)
  # raise right arm
  await myRobot.accessoryRight.run_target(500,0)

  # return home backwards



def mission1(myRobot,myOdometer):
  print("===== MISSION 1 =======")
  watch = myOdometer.watch

  async def odo(robot_pos):
    await myOdometer.run(robot_pos[0],robot_pos[1],robot_pos[2])

  robot_pos = [path[0][0],path[0][1], 90]   # mm, mm, degrees

  async def main():
    await multitask(odo(robot_pos),runMission(myRobot,myOdometer),race=True)

  run_task(main())


