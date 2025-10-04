"""
Motion profiling for motors

- Localize motors
- PID for motors to and from specific position
- Planning for multimotor movements

"""

"""

initialize motors

set torque
set initial position
set some target position

"""

from dynamixel_sdk import *

ADDR_TORQUE_ENABLE      = 64
ADDR_GOAL_POSITION      = 116
ADDR_PRESENT_POSITION   = 132

PROTOCOL_VERSION        = 2.0
DXL_ID                  = 1
BAUDRATE                = 57600
DEVICENAME              = '/dev/ttyUSB0'

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

if not portHandler.openPort():
    print("Failed to open the port")
    exit()

if not portHandler.setBaudRate(BAUDRATE):
    print("Failed to set baudrate")
    exit()

# Enable torque
packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, 1)

# Move motor
packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, 2048)

# Wait and read position
import time
time.sleep(1)
position, _, _ = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)
print("Motor is at:", position)

# Disable torque and close
packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, 0)
portHandler.closePort()
