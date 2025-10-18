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
<<<<<<< HEAD
DEVICENAME              = '/dev/ttyUSB0'
=======
DEVICENAME              = 'COM3'
>>>>>>> 6bcbea24c052d0753ee81ec2302f04b30988c831

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

@@ -42,12 +46,29 @@ if not portHandler.setBaudRate(BAUDRATE):
# Enable torque
packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, 1)

<<<<<<< HEAD
# Move motor
packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, 2048)

# Wait and read position
import time
time.sleep(1)
=======
position, _, _ = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)
print("Motor is at:", position)

# Move motor
packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, 10)

# Wait and read position
import time
time.sleep(3)
position, _, _ = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)
print("Motor is at:", position)

# Reset encoder count to 0
packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION, 0)
>>>>>>> 6bcbea24c052d0753ee81ec2302f04b30988c831
position, _, _ = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)
print("Motor is at:", position)
