from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from robot import robotCompetition
#from odometer import odometer

from testConfig import program1, program0
from testOdometer import program2
from testPursuit import testPursuit
from mission1 import mission1
from mission3_4 import mission3_4
from mission9 import mission9
#from mission7 import mission7
from mission8_b import mission8
from mission10 import mission10
from mission12 import mission12
from mission956 import mission956
from mission14 import mission14

watch = StopWatch()
myRobot = robotCompetition()
#myOdometer = odometer(myRobot,watch);

color = myRobot.colorSensor.color()
print("sensed color:",color)

MissionTable = [[Color.NONE,"A",program0], # config test, battery level
                [Color.LIGHTBROWN,"B",program1], # test configuration with motion
                [Color.DARKBROWN,"C",program2],  # test odometer
#                [Color.BEIGE,"D",testPursuit], # test trajectory tracking
                [Color.YELLOW,"1",mission1],
                [Color.ROSE,"2",mission956],
                [Color.MAGENTA,"3",mission10],
                [Color.LIGHTBLUE,"4",mission8],
                [Color.DARKBLUE,"4",mission8],
                [Color.WHITE,"5",mission12],
                [Color.BLACK,"6",mission3_4],
                [Color.RED,"7",mission14],
                ]  

for mission in MissionTable:
    if (color == mission[0]):
        print(mission)
#        myRobot.hub.display.char(str(mission[1]))
        myRobot.hub.display.char(mission[1])
        print("Running program ",mission[1])
#        mission[2](myRobot,myOdometer)
        mission[2](myRobot)

myRobot.accessoryLeft.stop()
myRobot.accessoryRight.stop()
myRobot.driveBase.stop()

wait(500)