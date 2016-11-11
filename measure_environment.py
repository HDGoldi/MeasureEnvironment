#!/usr/bin/python3
import configparser
import socket
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'user': '',
    'password': '',
    'host': 'localhost',
    'database': 'envmon'
}

class Data:
    """Data from the SenseHat"""
    def __init__(self, sensehat):
        self.humidity = sensehat.get_humidity()
        self.temperature_from_humidity = sensehat.get_temperature_from_humidity()
        self.temperature_from_pressure = sensehat.get_temperature_from_pressure()
        self.pressure = sensehat.get_pressure()
        self.orientation = sensehat.get_orientation_radians()
        self.compass = sensehat.get_compass_raw()
        self.gyroscope = sensehat.get_gyroscope_raw()
        self.accelerometer = sensehat.get_accelerometer_raw()

    def sql_fields(self):
        result = "("
        result += "sensor, humidity, pressure"
        result += ", temperature_from_humidity, temperature_from_pressure"
        result += ", orientation_pitch, orientation_roll, orientation_yaw"
        result += ", compass_x, compass_y, compass_z"
        result += ", gyroscope_pitch, gyroscope_roll, gyroscope_yaw"
        result += ", accelerometer_pitch, accelerometer_roll, accelerometer_yaw"
        result += ")"
        return result;

    def to_sql(self):
        result = "("
        result += "'" + socket.gethostname() + "', " + str(self.humidity) + ", " + str(self.pressure)
        result += ", " + str(self.temperature_from_humidity) + ", " + str(self.temperature_from_pressure)
        result += ", " + str(self.orientation["pitch"]) + ", " + str(self.orientation["roll"]) + ", " + str(self.orientation["yaw"])
        result += ", " + str(self.compass["x"]) + ", " + str(self.compass["y"]) + ", " + str(self.compass["z"])
        result += ", " + str(self.gyroscope["x"]) + ", " + str(self.gyroscope["y"]) + ", " + str(self.gyroscope["z"])
        result += ", " + str(self.accelerometer["x"]) + ", " + str(self.accelerometer["y"]) + ", " + str(self.accelerometer["z"])
        result += ")"
        return result
 
def generate_sql_insert_statement(data):
    statement = "INSERT INTO envdata" + data.sql_fields()
    statement += " VALUES" + data.to_sql()
    statement += ";"
    return statement;

data = Data(sense)

print("Humidity: %s %%rH" % data.humidity)
print("Temperature: %s C" % data.temperature_from_humidity)
print("Temperature: %s C" % data.temperature_from_pressure)
print("Pressure: %s Millibars" % data.pressure)
print("Orientation p: {pitch}, r: {roll}, y: {yaw}".format(**data.orientation))
print("Compass x: {x}, y: {y}, z: {z}".format(**data.compass))
print("Gyroscope x: {x}, y: {y}, z: {z}".format(**data.gyroscope))
print("Accelerometer x: {x}, y: {y}, z: {z}".format(**data.accelerometer))

print("")
statement = generate_sql_insert_statement(data)
print(statement)
print("")
