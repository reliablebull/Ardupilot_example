import time
import dronekit

vehicle = dronekit.connect(ip="127.0.0.1:14550",wait_ready=True)

vehicle.armed = True


time.sleep(5)


vehicle.armed = False

time.sleep(5)

vehicle.mode = dronekit.VehicleMode("GUIDED")

time.sleep(5)

print("Mode : " , vehicle.mode.name)

vehicle.close()