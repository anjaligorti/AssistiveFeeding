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
ADDR_VELOCITY_PROFILE   = 112


PROTOCOL_VERSION        = 2.0
DXL_ID                  = 1
BAUDRATE                = 57600
DEVICENAME              = 'COM3'

ENCODER_TO_DEGREE_CONT = 4085/360

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

position, _, _ = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)
print("Motor is at:", position)

# Move motor
packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, 2000)
# Wait and read position
import time
time.sleep(3)
position, _, _ = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)
print("Motor is at:", position)

packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_VELOCITY_PROFILE, 100)

# Disable torque and close
packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, 0)
portHandler.closePort()

def ending_sequence():
    motor_move(DXL_ID, 0, 3)
    # Disable torque and close
    packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, 0)
    portHandler.closePort()




def motor_move(motor_id, target_position, speed):
    pass

def update_speed(speed):
    ADDR_VELOCITY_LIMIT = 44  # 4 bytes

    # Example: set limit to 200 (units depend on model)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
        portHandler, DXL_ID, ADDR_VELOCITY_LIMIT, speed
    )
    if dxl_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print(packetHandler.getRxPacketError(dxl_error))
    else:
        print("Velocity limit updated to 200.")


"""
Safety feature:
when voltage drops, we can have a fail safe that will move to a safe position
turn off mode that doesn't rely on the behavior of the motors



"""
