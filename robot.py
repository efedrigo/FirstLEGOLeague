from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis, Icon
from pybricks.robotics import DriveBase
from pybricks.iodevices import PUPDevice
from pybricks.tools import wait
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
    wheelDiameter = 0;
    wheelC = 0;
    axle=0

    def __init__(self):
        self.hub = InventorHub(front_side=Axis.X,top_side=Axis.Z);
        self.motorLeft = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE);
        self.motorRight = Motor(Port.B,positive_direction=Direction.CLOCKWISE);
        self.wheelDiameter = 88.6; # mm
        self.wheelC = self.wheelDiameter * umath.pi; #mm
        self.axle = 88; #mm

##################################################
#
#
#
##################################################
class robotCompetition():
    hub = 0;
    motorLeft = 0;
    motorRight = 0;
    wheelDiameter = 0;
    wheelC = 0;
    axle=0
    driveBase=0;
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
        # id 49 : new large motor
        # id 48 : new medium motor
        # id 75 : old medium motor
            id = device.info()["id"]
            if (port == Port.A):        
                if (id == 49):
                    print(port,": New large motor,correct")
                elif (id == 75):
                    print(port,": Old medium motor,correct")
                else:
                    print("Port A is not connected to a new large or old medium motor, id: ",id)
                    self.configurationCorrect = False
            elif (port ==Port.B):        
                if (id == 49):
                    print(port,": New large motor,correct")
                elif (id == 75):
                    print(port,": Old medium motor,correct")
                else:
                    print("Port B is not connected to a new large or old medium motor, id: ",id)
                    self.configurationCorrect = False
            elif (port == Port.C):        
                if (id == 48):
                    print(port,": New medium motor, correct")
                elif (id == 75):
                    print(port,": Old medium motor,correct")
                else:
                    print("Port C is not connected to a medium motor, id: ",id)
                    self.configurationCorrect = False
            elif (port == Port.D):        
                if (id == 48):
                    print(port,": New medium motor, correct")
                elif (id == 75):
                    print(port,": Old medium motor,correct")
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
        self.hub = InventorHub(front_side=-Axis.X,top_side=Axis.Z);
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

        # blue : 87.5 m
        # black-motorcycle:81.6
            self.wheelDiameter = 79.78; # diameter, mm
            self.wheelC = self.wheelDiameter * umath.pi; #mm 
            self.axle = 89; #88; #mm
            self.driveBase = DriveBase(self.motorLeft, 
                                       self.motorRight, 
                                       wheel_diameter=self.wheelDiameter, 
                                       axle_track=self.axle)
            self.driveBase.use_gyro(True)
            self.driveBase.reset(0,0)
            print("drivebase:",self.driveBase.settings())
        print("init done")

    def runStraight(self,speed,distance):
        self.driveBase.settings(speed,1000,300,1200); # speed, accel, angular speed, angular accel
        print("runStraight start:",self.driveBase.distance())
        self.driveBase.straight(distance,then=Stop.HOLD,wait=True)
        while not self.driveBase.done():
            wait(10)
        print("runStraight end:",self.driveBase.distance())
    
    def rotate(self,degrees):
        self.driveBase.settings(500,1000,300,1200); # speed, accel, angular speed, angular accel
        actual_angle=self.driveBase.angle();   
        print("rotate start:",actual_angle)
        self.driveBase.turn(degrees,then=Stop.HOLD, wait=True)

        new_angle = self.driveBase.angle();
        print("rotate end:",new_angle)
        if (abs(new_angle-actual_angle) < abs(degrees)-1):
            print("rotate incomplete, retrying")
            self.driveBase.turn(degrees-(new_angle-actual_angle),then=Stop.HOLD, wait=True)

        new_angle = self.driveBase.angle();
        print("rotate end:",new_angle)

    # rotate from the current angle to an absolute angle as given by the gyro
    # the second parameter indicates how may times to retry in case the rotation could not be completed
    # on the first try, likely due to un obstacle
    # if the second parameter is 0, an uncontrolled rotation is performed without gyro assistance
    # in this case the robot should not insist too much in case of an obstacle
    # the result will not be the final angle and this condition can be detecte
    # if the parameter is 1 or more or default, the robot will retry until the angle is reached
    # which will force a lateral motion of the robot in case of an obstacle

    def rotateAbs(self,degrees,try_number=3):
        self.driveBase.settings(500,1000,300,1200); # speed, accel, angular speed, angular accel
        actual_angle=self.hub.imu.heading();   
        target=degrees-actual_angle

#        print("rotate start:",actual_angle)
        if (try_number<=0):
            self.driveBase.use_gyro(False)
        else:
            self.driveBase.use_gyro(True) 

        self.driveBase.turn(target,then=Stop.HOLD, wait=True)

        new_angle = self.hub.imu.heading();
        if (abs(new_angle-degrees)>10):
            print("**** Likely impact detected on rotation")
            if (try_number<=0):
                self.driveBase.use_gyro(True) 
                return
            
#        print("rotate end:",new_angle)
        i=0
        while (abs(new_angle-degrees)>1 and i<try_number):
#            print("rotate incomplete, retrying:",degrees-new_angle)
            self.driveBase.turn(degrees-new_angle,then=Stop.HOLD, wait=True)
            new_angle = self.hub.imu.heading();
#            print("rotate end:",new_angle)
            i+=1

        new_angle = self.hub.imu.heading();
#        print("rotate end:",new_angle)
        self.driveBase.reset(0,new_angle)
        self.driveBase.use_gyro(True) 



    def curve(self,radius,speed,degrees):
        print("curve start:",self.driveBase.angle())
        self.driveBase.settings(speed,1000,300,1200); # speed, accel, angular speed, angular accel
        self.driveBase.arc(radius,degrees,then=Stop.HOLD, wait=True)
        print("curve end:",self.driveBase.angle())
