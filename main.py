from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from odometer import odometer

hub = InventorHub(front_side=-Axis.X)
watch = StopWatch()
motorLeft = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE)
motorRight = Motor(Port.B,positive_direction=Direction.CLOCKWISE)

print(hub)

#try:
#    accessoryLeft = Motor(port=Port.C)
#except:
#    print("No motor C")

#accessoryRight = Motor(Port.D)

D=100;
wheelC = 88.6 * umath.pi;

myOdometer = odometer(hub,watch,motorLeft,motorRight,wheelC,D);

start=watch.timeus()/1000; # seconds

#accessoryLeft.run_angle(50,90) #move at 50 deg/s to 90 deg

async def move():
    print("move start")

    motorLeft.run(500)
    motorRight.run(500)
    await wait(1500)

    motorLeft.run(300)
    motorRight.run(500)
    await wait(1500)

    motorLeft.run(600)
    motorRight.run(400)
    await wait(3800)

    motorLeft.run(500)
    motorRight.run(500)
    await wait(1500)

    motorLeft.run(400)
    motorRight.run(500)
    await wait(800)

    motorLeft.run(500)
    motorRight.run(400)
    await wait(800)

    motorLeft.hold()
    motorRight.hold()

    motorLeft.run(-400)
    motorRight.run(-400)
    await wait(450)

    motorLeft.hold()
    motorRight.hold()

    motorLeft.run(-400)
    motorRight.run(400)
    await wait(700)

    motorLeft.hold()
    motorRight.hold()

    print("move stop")

    encR=motorRight.angle()
    encL=motorLeft.angle();

    print(encR,encL)

    motorLeft.stop()
    motorRight.stop()

async def odo():
    await myOdometer.run()

#run_task(odo())
async def main():
#    await multitask(move(),myOdometer.run(),race=True)
    await multitask(move(),odo(),race=True)

run_task(main())

pos=myOdometer.getPosition()
print(0,",",pos[0],",",pos[1],",",pos[2],",",pos[3])
