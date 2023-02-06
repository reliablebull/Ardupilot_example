import dronekit

print("Trying to connect to the vehicle...")

vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)

print("Connected to the vehicle.")

print("mode :" + vehicle.mode.name)

vehicle.close()