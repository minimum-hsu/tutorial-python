
from influxdb_client_3 import InfluxDBClient3


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
def query_sensor_data():
    with InfluxDBClient3(host=INFLUXDB_URL, token=TOKEN, database=DATABASE) as client:
        sql = "SELECT * FROM sensor_data ORDER BY time DESC LIMIT 10"
        df = client.query(query=sql, mode="pandas")
        print(df)


#############################
# Main
#############################
if __name__ == "__main__":
    query_sensor_data()
