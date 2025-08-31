#
# 2D odometer
#

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import umath

###############################################################

class odometer():
    hub = 0;
    watch = 0;
    motorL = 0;
    motorR = 0;
    wheelC = 0;
    D = 1;
    t_prev = 0;
    encR_prev = 0;
    encL_prev =0;
    X=0;
    Y=0;
    theta=0;
    yaw = 0;
    collision = False;

  #  XA = [];
  #  YA = [];
  #  thetaA = [];
  #  yawA = [];
    

    def __init__(self,myRobot,watch):
        print("Odometer constructor")
        self.hub = myRobot.hub;
        self.watch = watch;
        self.wheelC = myRobot.wheelC;
        self.motorL = myRobot.motorLeft;
        self.motorR = myRobot.motorRight;
        self.D = myRobot.D;
    
    def start(self,posX,posY,yaw):
        print("odomoter start",posX,posY,yaw)
# if modified kernel
        #self.t_prev = watch.timeus()/1000; # mseconds
# otherwise
        self.t_prev=self.watch.time(); #mseconds

        self.encR_prev=self.motorR.angle()
        self.encL_prev=self.motorL.angle();

        self.X=posX;
        self.Y=posY;
        self.theta=yaw/180*umath.pi;
        self.yaw = yaw;
        self.collision = False;
        self.hub.imu.reset_heading(self.yaw);
    
    def getPosition(self):
        return [self.X,self.Y,self.theta/umath.pi*180.0,self.yaw,self.collision];

    def runOnce(self):
# if modified kernel
        #t = self.watch.timeus()/1000; # mseconds
# otherwise
        t = self.watch.time(); #mseconds
        
        encR=self.motorR.angle()
        encL=self.motorL.angle();
        self.yaw = self.hub.imu.heading();     # degrees
#        speedR = self.motorR.speed()
#        speedL = self.motorL.speed()
 #       yaw_rate = self.hub.imu.angular_velocity(Axis.Z)

        deltaT=t-self.t_prev;
        delta_encR=encR-self.encR_prev;
        delta_encL=encL-self.encL_prev;

        if (delta_encR == 0 and delta_encL == 0):
            return [self.X,self.Y,self.theta/umath.pi*180.0,self.yaw, self.collision]
        
        if (encR-self.encR_prev<-180):
            delta_encR += 360;
        if (encR-self.encR_prev>180):
            delta_encR -= 360;
        if (encL-self.encL_prev<-180):
            delta_encL += 360;
        if (encL-self.encL_prev>180):
            delta_encL -= 360;
  
        self.t_prev=t;
        self.encR_prev = encR;
        self.encL_prev = encL;

        deltaR=delta_encR/360.0*self.wheelC;
        deltaL=delta_encL/360.0*self.wheelC;
        deltaS=(deltaR+deltaL)/2;
#        deltaTheta=(deltaR-deltaL)/self.D;
#        print(deltaS,self.theta)
  
        deltaVR=deltaR/deltaT;
        deltaVL=deltaL/deltaT;
#        deltaV=(deltaVR+deltaVL)/2;
        omega = (deltaVR-deltaVL)/self.D;

#        self.theta=self.theta+omega*deltaT; # computed from encoders, not gyro!
        self.theta=self.yaw/180.0*umath.pi+omega*deltaT; # computed from gyro!
    
        self.X=self.X+deltaS*umath.cos(self.theta);
        self.Y=self.Y+deltaS*umath.sin(self.theta); 

        if (abs(self.yaw-self.theta/umath.pi*180)>20):
            self.collision = True;
        
        return [self.X,self.Y,self.theta/umath.pi*180.0,self.yaw, self.collision]

    async def run(self,posX,posY,yaw):
        loop=True;
        n=0;

        self.start(posX,posY,yaw);

        print("---- ODOMETER ----------------")
        while loop:
            pos = self.runOnce();
            n=n+1
            if (n%5 == 0):
                print(n,",",pos[0],",",pos[1],",",pos[2],",",pos[3],",",1 if pos[4] else 0)

            await wait(10)

    def runAccumulate(self):
        loop=True;
        self.start();
        print("---- ODOMETER ACC ----------------")
        while loop:
            pos = self.runOnce();

            self.XA.append(pos[0]);
            self.YA.append(pos[1]);
            self.thetaA.append(pos[2]);
            self.yawA.append(pos[3])

            wait(10)

    def getXA(self):
        return self.XA;

    def getYA(self):
        return self.YA;

    def getXA(self):
        return self.XA;

    def getXA(self):
        return self.XA;

    def getXY(self):
        return [self.X,self.Y]

    def getPos(self):
        return [self.X,self.Y,self.theta]

    def getPosFull(self):
        return [self.X,self.Y,self.theta,self.yaw]
