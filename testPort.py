from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from uerrno import ENODEV

# Make a list of known ports.
ports = [Port.A, Port.B,Port.C]

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
    print(port, ":", "device with ID", id)
    wait(1000)


