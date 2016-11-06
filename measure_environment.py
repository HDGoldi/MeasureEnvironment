#!/usr/bin/python3
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)
print(sense.humidity)

temp1 = sense.get_temperature()
print("Temperature: %s C" % temp1)
print(sense.temp)
print(sense.temperature)

temp2 = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp2)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)
print(sense.pressure)

orientation = sense.get_orientation_radians()
print("Orientationn p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
print(sense.orientation_radians)

compass = sense.get_compass_raw()
print("Compass x: {x}, y: {y}, z: {z}".format(**compass))
print(sense.compass_raw)

gyro = sense.get_gyroscope_raw()
print("Gyroscope x: {x}, y: {y}, z: {z}".format(**gyro))
print(sense.gyro)
print(sense.gyroscope)

accel = sense.get_accelerometer_raw()
print("Accelerometer x: {x}, y: {y}, z: {z}".format(**accel))
print(sense.accel)
print(sense.accelerometer)
