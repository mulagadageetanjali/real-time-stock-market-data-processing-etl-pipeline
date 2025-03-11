import requests
import json
from kafka import KafkaProducer
import time
import os
from dotenv import load_dotenv



# Twelve Data API Key (Sign up at https://twelvedata.com )
API_KEY = os.getenv("API_KEY")
TICKER = "TSLA"
START_DATE="2021-01-01 00:00:00"
END_DATE="2022-03-03 00:00:00"
URL=f"https://api.twelvedata.com/time_series?apikey={API_KEY}&interval=1week&symbol={TICKER}&type=stock&start_date={START_DATE}&end_date={END_DATE}&outputsize=50"

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

def fetch_stock_data():
    response = requests.get(URL)
    data = response.json()
    
    if "values" in data:
        return data["values"]  # Return the entire list of stock records
    else:
        return []  # Return empty list if no data is found

while True:
    stock_records = fetch_stock_data()
    try:
        if stock_records:
            for record in stock_records:  # Iterate through each stock record
                stock_data = {
                    "ticker": "TSLA",
                    "price": float(record["close"]),
                    "volume": int(record["volume"]),
                    "timestamp": record["datetime"]
                }
                print(f"Sent: {stock_data}")  # Debugging print
                producer.send("stock_prices", stock_data)
    except Exception as e:
        print(f" Unexpected Error: {e}")
    except requests.exceptions.Timeout:
        print(" Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f" Network or HTTP error: {e}")
    except ValueError as ve:
        print(f" API Response Error: {ve}")

    time.sleep(20)  # Fetch data every 60 seconds (modify as needed)