
#####START
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 600
MEDIUM_FAST_SPEED = 400
MEDIUM_SPEED = 300
MEDIUM_SLOW_SPEED = 200
SLOW_SPEED = 100
DISTANCE1 = 380

def mission8(myRobot): # alternative
    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = -1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase
   
    # --- 1) vai avanti e dai delle martellate ---
    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=FAST_SPEED)

    # setta la posizione di partenza di ogni attachment
    myRobot.accessoryLeft.reset_angle(0)
    myRobot.accessoryRight.reset_angle(0)

    drive.straight(DISTANCE1, then=Stop.BRAKE, wait=True)

    """
    Per muoveere il martello, un ingranaggio piccolo (sul motore) è collegato ad uno grande (sull'attachment).
    L'ingranaggio piccolo ha 12 denti, il grande 20: per dare una martellata, il motore deve fare 20/12=5/3 giri.
    Non posso usare run_target() per portare il martello ad una posizione fissa, perchè ad una certa posizione del 
    motore non corrisponde sempre la stessa posizione fissa del martello (cambia dopo ogni giro).
    """
    
    mart_num =   5.5  * 4/4*360 # il primo numero è il numero di martellate + mezza per fermare col martello basso
    mart_speed = 1.4  * 4/4*360 # il primo numero è il numero di martellate al secondo
    myRobot.accessoryRight.run_angle(mart_speed, mart_num, then=Stop.HOLD, wait=True)

    myRobot.accessoryRight.stop()
    

    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=FAST_SPEED)

    drive.turn(-80)
    drive.arc(-280,45)
    drive.straight(250, then=Stop.BRAKE, wait=True)
    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=MEDIUM_SPEED)
    myRobot.accessoryRight.run_angle(mart_speed, 180, then=Stop.HOLD, wait=False)
    drive.arc(100,45)
    myRobot.rotateAbs(-90)
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=SLOW_SPEED,turn_rate=100,turn_acceleration=200 )
    drive.straight(90, then=Stop.BRAKE, wait=True)
    drive.arc(-85,78)


    myRobot.accessoryLeft.run(-550)
    wait(4*1000)
    myRobot.accessoryLeft.stop()
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=FAST_SPEED)
    drive.straight(-100)

    angle=-92;
    drive.arc(-120,angle)
    myRobot.rotateAbs(angle)
    drive.straight(1100)

    return



