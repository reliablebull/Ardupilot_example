import time
import pymavlink.mavutil
import pymavlink.dialects.v20.all as dialect


vehicle = pymavlink.mavutil.mavlink_connection(device="udpin:127.0.0.1:14550")

vehicle.wait_heartbeat()

print("Connected to the vehicle")

print("Target system" , vehicle.target_system , "Target componenet : " , vehicle.target_component)



# message interv  al command

set_message_request_command = dialect.MAVLink_command_long_message(
                                                target_system=vehicle.target_system,
                                                target_component = vehicle.target_component,
                                                command=dialect.MAV_CMD_REQUEST_MESSAGE,
                                                confirmation=0,
                                                param1=dialect.MAVLINK_MSG_ID_AUTOPILOT_VERSION,
                                                param2=0,
                                                param3=0,
                                                param4=0,
                                                param5=0,
                                                param6=0,
                                                param7=0
)



vehicle.mav.send(set_message_request_command)


while True:
    message = vehicle.recv_match(type=dialect.MAVLink_autopilot_version_message.msgname , blocking=True)

    message = message.to_dict()


    print("major:" , message["flight_sw_version"] >> 24 & 0xff)
    print("minor:" , message["flight_sw_version"] >> 16 & 0xff)
    print("patch:" , message["flight_sw_version"] >> 8 & 0xff)
