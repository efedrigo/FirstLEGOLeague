from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis, Icon
from pybricks.robotics import DriveBase
from pybricks.iodevices import PUPDevice
from uerrno import ENODEV
import umath

Color.LIGHTGREEN = Color(h=72, s=46, v=13)
Color.DARKGREEN = Color(h=135, s=51, v=9)
Color.MAGENTA = Color(h=260, s=51, v=5)
Color.FUCSIA = Color(h=338, s=81, v=9)
Color.ROSE = Color(h=330, s=64, v=24)
Color.RED = Color(h=348, s=88, v=15)
Color.DARKBLUE = Color(h=223, s=75, v=9)
Color.LIGHTBLUE = Color(h=208, s=71, v=17)
Color.YELLOW = Color(h=42, s=78, v=26)
Color.LIGHTBROWN = Color(h=0, s=65, v=11)
Color.DARKBROWN = Color(h=345, s=64, v=5)
Color.BEIGE = Color(h=21, s=49, v=19)
Color.BLACK = Color(h=300, s=29, v=3)
Color.WHITE = Color(h=348, s=20, v=31)
Color.LIGHTGRAY = Color(h=270, s=20, v=13)
Color.NONE = Color(h=330, s=88, v=1)

# Put your colors in a list or tuple.
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
        self.wheelC = 88.6 * umath.pi; #mm
        self.D = 88; #mm

class robotCompetition():
    hub = 0;
    motorLeft = 0;
    motorRight = 0;
    wheelC = 0;
    D = 0;
    configurationCorrect = False;

    def testConfig(self):
# Make a list of known ports.
        ports = [Port.A, Port.B,Port.C, Port.D, Port.E,Port.F]

        self.configurationCorrect = True

# Go through all available ports.
        for port in ports:

    # Try to get the device, if it is attached.
            try:
                device = PUPDevice(port)
            except OSError as ex:
                if ex.args[0] == ENODEV:
                # No device found on this port.
                    print(port, ": empty")
                    continue
                else:
                    raise

    # Get the device id
            id = device.info()["id"]
            if (port == Port.A):        
                if (id == 49):
                    print(port,": Large motor,correct")
                else:
                    print("Port A is not connected to a Large motor, id: ",id)
                    self.configurationCorrect = False
            elif (port ==Port.B):        
                if (id == 49):
                    print(port,": Large motor, correct")
                else:
                    print("Port B is not connected to a Large motor, id: ",id)
                    self.configurationCorrect = False
            elif (port == Port.C):        
                if (id == 48):
                    print(port,": Medium motor, correct")
                else:
                    print("Port C is not connected to a medium motor, id: ",id)
                    self.configurationCorrect = False
            elif (port == Port.D):        
                if (id == 48):
                    print(port,": Medium motor, correct")
                else:
                    print("Port D is not connected to a medium motor, id: ",id)
                    self.configurationCorrect = False;
            elif (port == Port.E):        
                if (id == 61):
                    print(port,": color sensor, correct")
                else:
                    print("Port E is not connected to a color sensor, id: ",id)
                    self.configurationCorrect = False
        return self.configurationCorrect

    def __init__(self):
        self.hub = InventorHub(front_side=-Axis.X,top_side=-Axis.Z);
        self.hub.display.orientation(up=Side.RIGHT)
        self.hub.display.icon(Icon.CIRCLE)
        if (self.testConfig()):
            self.motorLeft = Motor(Port.A,positive_direction=Direction.CLOCKWISE);
            self.motorRight = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE);
            self.accessoryLeft = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE);
            self.accessoryRight = Motor(Port.D,positive_direction=Direction.CLOCKWISE);
            self.colorSensor = ColorSensor(Port.E)
    # Save your colors.
            self.colorSensor.detectable_colors(my_colors)

        # blue : 87m.5 m
        # black-motorcycle:81.6
        self.wheelC = 81.6 * umath.pi; #mm 
        self.D = 88; #mm

