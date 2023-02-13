import time
import pymavlink.mavutil
import pymavlink.dialects.v20.all as dialect


SYSID_THISMAV = "SYSID_THISMAV"

vehicle = pymavlink.mavutil.mavlink_connection(device="udpin:127.0.0.1:14550")

parameter_request_list_message = dialect.MAVLink_param_request_list_message(
    target_system = vehicle.target_system,
    target_component=vehicle.target_component
)

parameter_request_message = dialect.MAVLink_param_request_read_message(
    target_system = vehicle.target_system,
    target_component=vehicle.target_component,
    param_id= SYSID_THISMAV.encode("utf-8"),
    param_index = 1
)

parameter_set_message = dialect.MAVLink_param_set_message(
    target_system = vehicle.target_system,
    target_component=vehicle.target_component,
    param_id = SYSID_THISMAV.encode("utf-8"),
    param_value=1,
    param_type=dialect.MAV_PARAM_TYPE_REAL32
)

vehicle.wait_heartbeat()

print("Connected to the vehicle")

print("Target system" , vehicle.target_system , "Target componenet : " , vehicle.target_component)


# vehicle.mav.send(parameter_request_list_message)
vehicle.mav.send(parameter_set_message)

while True:

    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname, blocking=True)
    message = message.to_dict()

    if message["param_id"] == SYSID_THISMAV:
        print(message['param_id'] , message['param_value'])

        #break

#vehicle.mav.send()
    #print(vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname, blocking=True).to_dict())