
from influxdb_client_3 import InfluxDBClient3
from influxdb_client_3 import Point
from datetime import datetime
from datetime import timezone

#############################
# Environment Variables
#############################
import os
from dotenv import load_dotenv

load_dotenv()
INFLUXDB_URL = os.getenv("INFLUXDB_URL")
TOKEN = os.getenv("INFLUXDB_TOKEN")
DATABASE = os.getenv("INFLUXDB_DATABASE")


#############################
# Functions
#############################
def write_sensor_data(data):
    with InfluxDBClient3(host=INFLUXDB_URL, token=TOKEN, database=DATABASE) as client:
        point = Point("sensor_data") \
            .tag("device", data["device"]) \
            .field("temperature", data["temperature"]) \
            .field("humidity", data["humidity"]) \
            .time(data["timestamp"])
        client.write(point)
        print("Data written:", data)


#############################
# Main
#############################
if __name__ == "__main__":
    data = {
        "device": "sensor-01",
        "temperature": 23.5,
        "humidity": 60.2,
        "timestamp": datetime.now(timezone.utc)
    }
    write_sensor_data(data)
