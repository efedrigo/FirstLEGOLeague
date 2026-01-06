from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from robot import robotCompetitionCompact
#from odometer import odometer

from testConfig import program1, program0
from testOdometer import program2
from testPursuit import testPursuit
from mission1 import mission1
from mission3_4 import mission3_4
from mission9 import mission9
#from mission7 import mission7
from mission8 import mission8
from mission10 import mission10
from mission12 import mission12
from mission956 import mission956

watch = StopWatch()
myRobot = robotCompetitionCompact()
#myOdometer = odometer(myRobot,watch);

# START DEBUG
# mybrightness = 100
# while mybrightness>0:
#         myRobot.colorSensor.lights.on(mybrightness)
#         wait(1000)
#         color = myRobot.colorSensor.color()
#         print("sensed color:",color,"at brightness:",mybrightness,"%")
#         mybrightness = mybrightness - 10
# END DEBUG

color = myRobot.colorSensor.color()
print("sensed color:",color)


MissionTable = [[Color.NONE,0,program0], # config test
                [Color.LIGHTBROWN,1,program1], # test configuration with motion
                [Color.DARKBROWN,2,program2],  # test odometer
                [Color.BEIGE,3,testPursuit], # test trajectory tracking
                [Color.YELLOW,4,mission1],
                [Color.BLACK,5,mission3_4],
                [Color.MAGENTA,6,mission10],
                [Color.LIGHTBLUE,7,mission8],
                [Color.DARKBLUE,8,mission8],
                [Color.WHITE,9,mission956], #was mission12
                [Color.ROSE,10,mission956],
                ]   

for mission in MissionTable:
    if (color == mission[0]):
        print(mission)
        myRobot.hub.display.char(str(mission[1]))
        print("Running program",mission[1])
#        mission[2](myRobot,myOdometer)
        mission[2](myRobot)

wait(500)
