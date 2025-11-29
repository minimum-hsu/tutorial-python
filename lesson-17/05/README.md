
# InfluxDB 3.7 + Python + pandas Example


This example demonstrates how to use Python 3 and the influxdb3-python library with pandas to write and query data in InfluxDB 3.7. All connection parameters are loaded from a `.env` file.

docker compose up -d

## Step 1: Start InfluxDB 3.7 (Official Docker)

```bash
docker compose up -d
```
- Default API port: 8181
- Data directories are configured in docker-compose.yml



## Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

本範例使用 [python-dotenv](https://pypi.org/project/python-dotenv/) 來讀取 .env 檔案，請確保 requirements.txt 內有 `python-dotenv`。


## Step 3: Obtain InfluxDB 3.7 Token

InfluxDB 3.7 uses its own CLI for token management. Do NOT use SQL commands to create tokens.

1. Create an operator (admin) token using the official CLI:
    ```bash
    docker exec -it influxdb3-core influxdb3 create token --admin
    ```
    - This will create an admin token and print it to the console.
    - Copy this token and use it as the `INFLUXDB_TOKEN` value in your `.env` file.

2. Store your token securely. You cannot retrieve it again from the database later.

For more details, see the [InfluxDB 3.7 official documentation](https://docs.influxdata.com/influxdb3/core/get-started/setup/#set-up-authorization).


## Step 4: Configure .env

Create a `.env` file in this folder with the following content:

```
INFLUXDB_URL=http://localhost:8181
INFLUXDB_TOKEN=your_token_here
INFLUXDB_DATABASE=my_database
```


## Step 5: Write Data (write.py)
```python

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

```



## Step 6: Query Data (query.py)
```python

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

```

## References

- [InfluxDB 3 Python client](https://github.com/InfluxCommunity/influxdb3-python)
- [InfluxDB Docker Hub](https://hub.docker.com/_/influxdb)
- [InfluxDB 3 SQL Authentication](https://docs.influxdata.com/influxdb3/core/admin/tokens/)
- [Pandas](https://pandas.pydata.org/)
