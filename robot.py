from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
import umath

class robot():
    hub = 0;
    motorLeft = 0;
    motorRight = 0;
    wheelC = 0;
    D = 0;

    def __init__(self):
        self.hub = InventorHub(front_side=Axis.X,top_side=-Axis.Z);
        self.motorLeft = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE);
        self.motorRight = Motor(Port.B,positive_direction=Direction.CLOCKWISE);
        self.wheelC = 56 * umath.pi; #mm
        self.D = 80; #mm

