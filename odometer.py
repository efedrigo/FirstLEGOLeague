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

  #  XA = [];
  #  YA = [];
  #  thetaA = [];
  #  yawA = [];
    

    def __init__(self,hub,watch,motorLeft,motorRight,wheelC,D):
        print("Odometer constructor")
        self.hub = hub;
        self.watch = watch;
        self.wheelC = wheelC;
        self.motorL = motorLeft;
        self.motorR = motorRight;
        self.D = D;
        self.start();
    
    def start(self):
        print("odomoter start")
        self.t_prev=self.watch.timeus()/1000;
        self.encR_prev=self.motorR.angle()
        self.encL_prev=self.motorL.angle();

        self.X=0;
        self.Y=0;
        self.theta=0;
        self.yaw = 0;
    
    def getPosition(self):
        return [self.X,self.Y,self.theta,self.yaw];

    def runOnce(self):
        t = self.watch.timeus()/1000;
        encR=self.motorR.angle()
        encL=self.motorL.angle();
        self.yaw = self.hub.imu.heading();     # degrees
#        speedR = self.motorR.speed()
#        speedL = self.motorL.speed()
        yaw_rate = self.hub.imu.angular_velocity(Axis.Z)

        deltaT=t-self.t_prev;
        delta_encR=encR-self.encR_prev;
        delta_encL=encL-self.encL_prev;

        if (delta_encR == 0 and delta_encL == 0):
            return [self.X,self.Y,self.theta,self.yaw]
        
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

        deltaR=delta_encR/360*self.wheelC;
        deltaL=delta_encL/360*self.wheelC;
        deltaS=(deltaR+deltaL)/2;
#        deltaTheta=(deltaR-deltaL)/self.D;
#        print(deltaS,self.theta)
  
        deltaVR=deltaR/deltaT;
        deltaVL=deltaL/deltaT;
        deltaV=(deltaVR+deltaVL)/2;
        omega = (deltaVR-deltaVL)/self.D;

        self.theta=self.theta+omega*deltaT; # computed from encoders, not gyro!
    
        self.X=self.X+deltaS*umath.cos(self.theta);
        self.Y=self.Y+deltaS*umath.sin(self.theta); 

        return [self.X,self.Y,self.theta,self.yaw]

    async def run(self):
        loop=True;
        n=0;

        self.start();

        print("---- ODOMETER ----------------")
        while loop:
            pos = self.runOnce();
            n=n+1
            if (n%10 == 0):
                print(n,",",pos[0],",",pos[1],",",pos[2],",",pos[3])

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
