from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from robot import robotCompetition



def show_battery_level(hub,current_voltage):
    
    hub.display.off()    
    led_on_crit_full = [6000, 6400, 6800, 7200, 8300]

    for led_y in range (5):  
        for led_x in range (5):
            if current_voltage >= led_on_crit_full[led_y]:
                hub.display.pixel(led_x,led_y,100)                             
       
    wait(3000)
show_battery_level()

def program0(myRobot):
    wait(1000)
    if (myRobot.testConfig()):
        myRobot.hub.display.icon(Icon.HAPPY)
    else:
        myRobot.hub.display.icon(Icon.SAD)
    wait(1000)

    current_voltage = myRobot.hub.battery.voltage()
    show_battery_level(myRobot.hub,current_voltage)

def program1(myRobot):

    wait(1000)

    myRobot.hub.display.icon(Icon.CIRCLE)
    color = myRobot.colorSensor.color()
    print("sensed color:",color)
    hsv = myRobot.colorSensor.hsv(True)
    print(hsv)

    print("Test accessories left")
    myRobot.hub.display.icon(Icon.ARROW_LEFT_UP)
    myRobot.accessoryLeft.reset_angle(0);
    myRobot.accessoryLeft.run_angle(360,360);
    wait(1000)

    print("Test accessories right")
    myRobot.hub.display.icon(Icon.ARROW_RIGHT_UP)
    myRobot.accessoryRight.reset_angle(0)
    myRobot.accessoryRight.run_angle(360,360);
    wait(1000)

    print("Test motion left")
    myRobot.hub.display.icon(Icon.ARROW_LEFT)
    myRobot.motorLeft.reset_angle(0);
    #    motorLeft.run_angle(360,360);
    wait(1000)

    print("Test motion right")
    myRobot.hub.display.icon(Icon.ARROW_RIGHT)
    myRobot.motorRight.reset_angle(0);
    #   motorRight.run_angle(360,360);
    wait(1000)

    myRobot.hub.display.icon(Icon.HAPPY)
    wait(1000)

