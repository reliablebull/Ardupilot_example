import time
import pymavlink.mavutil
import pymavlink.dialects.v20.all as dialect


vehicle = pymavlink.mavutil.mavlink_connection(device="udpin:127.0.0.1:14560")


vehicle.wait_heartbeat()

print("Connected to the vehicle")

print("Target system" , vehicle.target_system , "Target componenet : " , vehicle.target_component)



while True:
    try:
        message = vehicle.recv_match(type=dialect.MAVLink_system_time_message.msgname, blocking=True)
        message = message.to_dict()

        for fieldname in dialect.MAVLink_system_time_message.fieldnames:
            if fieldname == "time_boot_ms":
                print(fieldname , message[fieldname])
        print(message.to_dict())
    except:
        print("no message received from vehicle")
    
    time.sleep(0.01)