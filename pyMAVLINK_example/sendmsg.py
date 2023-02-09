import time
import pymavlink.mavutil
import pymavlink.dialects.v20.all as dialect


vehicle = pymavlink.mavutil.mavlink_connection(device="udpin:127.0.0.1:14560")


vehicle.wait_heartbeat()

print("Target system" , vehicle.target_system , "Target componenet : " , vehicle.target_component)

message = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                                target_component = vehicle.target_component,
                                                command=dialect.MAV_CMD_DO_SEND_BANNER,
                                                confirmation=0,
                                                param1=0,
                                                param2=0,
                                                param3=0,
                                                param4=0,
                                                param5=0,
                                                param6=0,
                                                param7=0)


vehicle.mav.send(message)


while True:

    message = vehicle.recv_match(type=[
        dialect.MAVLink_statustext_message.msgname,
        dialect.MAVLink_command_ack_message.msgname],
        blocking=True)

    message = message.to_dict()

    print(message)