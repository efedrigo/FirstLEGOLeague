from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from uerrno import ENODEV

# Make a list of known ports.
ports = [Port.A, Port.B,Port.C, Port.D, Port.E,Port.F]

configurationCorrect = True

# Go through all available ports.
for port in ports:

    # Try to get the device, if it is attached.
    try:
        device = PUPDevice(port)
    except OSError as ex:
        if ex.args[0] == ENODEV:
            # No device found on this port.
            print(port, ": ---")
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
            configurationCorrect = False
    elif (port ==Port.B):        
        if (id == 49):
            print(port,": Large motor, correct")
        else:
            print("Port B is not connected to a Large motor, id: ",id)
            configurationCorrect = False
    elif (port == Port.C):        
        if (id == 48):
            print(port,": Medium motor, correct")
        else:
            print("Port C is not connected to a medium motor, id: ",id)
            configurationCorrect = False
    elif (port == Port.D):        
        if (id == 48):
            print(port,": Medium motor, correct")
        else:
            print("Port D is not connected to a medium motor, id: ",id)
            configurationCorrect = False;
    elif (port == Port.E):        
        if (id == 61):
            print(port,": color sensor, correct")
        else:
            print("Port E is not connected to a color sensor, id: ",id)
            configurationCorrect = False


    wait(100)

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


if (configurationCorrect):
    colorSensor = ColorSensor(Port.E)
    # Save your colors.
    colorSensor.detectable_colors(my_colors)
    color = colorSensor.color()
    print("sensed color:",color)
    hsv = colorSensor.hsv(True)
    print(hsv)

    # light green:  72,  46,  13.  // 70,55,13
    # dark green:  135,  51,   9   // 150, 51, 9
    # magenta:      260,  51,   5   // 280, 55,5
    # fucsia:      338,  81,   9.  // 342, 85, 11
    # rose:        330,  64,  24.  // 330, 64, 24
    # dark blue:   223,  75,   9   // 230, 70, 9
    # light blue:  208,  71,  17   // 205, 75, 17
    # yellow:       42,  78,  26   // 21,76,26
    # light brown:   0,  65,  11   // 0, 65, 11
    # dark brown:  345,  64,   5   // 345, 64, 5
    # beige:        21,  49,  19   // 21,49,19
    # black:       300,  29,   3.  // 0,29,3
    # white:       348,  20,  31
    # light gray:  270,  20,  13
    # red:         348,  88,  15
    # none:        330,  88,   1
    
    print("Test accessories")
    accessoryLeft = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE);
    accessoryRight = Motor(Port.D,positive_direction=Direction.CLOCKWISE);
    print("Test accessories left")
    accessoryLeft.reset_angle(0);
    accessoryLeft.run_angle(360,360);
    wait(1000)
    print("Test accessories right")
    accessoryRight.reset_angle(0);
    accessoryRight.run_angle(360,360);
    wait(1000)

    print("Test motion")
    motorLeft = Motor(Port.A,positive_direction=Direction.CLOCKWISE);
    motorRight = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE);

    print("Test motion left")
    motorLeft.reset_angle(0);
#    motorLeft.run_angle(360,360);
    wait(1000)
    print("Test motion right")
    motorRight.reset_angle(0);
 #   motorRight.run_angle(360,360);
    wait(1000)
