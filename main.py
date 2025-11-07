from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from robot import robotCompetition
from odometer import odometer

from testConfig import program1, program0
from testOdometer import program2

watch = StopWatch()
myRobot = robotCompetition()
myOdometer = odometer(myRobot,watch);

color = myRobot.colorSensor.color()
print("sensed color:",color)

MissionTable = [[Color.NONE,0,program0], # config test
                [Color.ROSE,1,program1], # test configuration with motion
                [Color.RED,2,program2]]  # test odometer

for mission in MissionTable:
    if (color == mission[0]):
        print(mission)
        myRobot.hub.display.char(str(mission[1]))
        print("Running program ",mission[1])
        mission[2](myRobot,myOdometer)

wait(1000)
