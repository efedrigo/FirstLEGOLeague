from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from robotcompact import robotCompetitionCompact
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

### START REPEATED BLOCK
### THIS IS REPEATED HERE BECAUSE IT WAS OVERWRITTEN BY IMPORTING FROM testConfig.py 
Color.LIGHTGREEN = Color(h=72, s=46, v=13)
Color.DARKGREEN = Color(h=135, s=51, v=9)
Color.MAGENTA = Color(h=260, s=51, v=5)
Color.FUCSIA = Color(h=338, s=81, v=9)
Color.ROSE = Color(h=324, s=46, v=32) # redefined
Color.RED = Color(h=348, s=88, v=15)
Color.DARKBLUE = Color(h=213, s=87, v=13) # redefined
Color.LIGHTBLUE = Color(h=208, s=71, v=17)
Color.YELLOW = Color(h=49, s=65, v=29) # redefined
Color.LIGHTBROWN = Color(h=0, s=65, v=11)
Color.DARKBROWN = Color(h=345, s=64, v=5)
Color.BEIGE = Color(h=21, s=49, v=19)
Color.BLACK = Color(h=240, s=22, v=5) # redefined
Color.WHITE = Color(h=180, s=3, v=32) # redefined
Color.LIGHTGRAY = Color(h=270, s=20, v=13)
Color.NONE = Color(h=330, s=88, v=1)
my_colors = (Color.LIGHTGREEN, 
             Color.DARKGREEN, 
             Color.MAGENTA, 
             Color.FUCSIA, 
             Color.ROSE, 
             Color.RED, 
             Color.DARKBLUE,
             Color.LIGHTBLUE,
             Color.YELLOW,
             Color.LIGHTBROWN,
             Color.DARKBROWN,
             Color.BEIGE,
             Color.BLACK,
             Color.WHITE,
             Color.LIGHTGRAY,
             Color.NONE)
### END REPEATED BLOCK

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

hsv = myRobot.colorSensor.hsv(surface=True)
print("sensed HSV values:",hsv)

color = myRobot.colorSensor.color()
print("sensed color:",color)

MissionTable = [[Color.NONE,"0",program0], # config test, battery level
                [Color.LIGHTBROWN,"1",program1], # test configuration with motion
                [Color.DARKBROWN,"2",program2],  # test odometer
                [Color.BEIGE,"3",testPursuit], # test trajectory tracking
                [Color.YELLOW,"4",mission1],
                [Color.BLACK,"5",mission3_4],
                [Color.MAGENTA,"6",mission10],
                [Color.LIGHTBLUE,"7",mission8],
                [Color.DARKBLUE,"7",mission8],
                [Color.WHITE,"A",mission956],
                [Color.ROSE,"A",mission956],
                ]    


for mission in MissionTable:
    if (color == mission[0]):
        print(mission)
        myRobot.hub.display.char(str(mission[1]))
        print("Running program",mission[1])
#        mission[2](myRobot,myOdometer)
        mission[2](myRobot)

wait(500)