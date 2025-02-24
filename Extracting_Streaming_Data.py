import requests
import json
from kafka import KafkaProducer
import time
import os
from dotenv import load_dotenv



# Twelve Data API Key (Sign up at https://twelvedata.com and get your free key)
API_KEY = os.getenv("API_KEY")
TICKER = "FTSLO"
URL = f"https://api.twelvedata.com/time_series?symbol={TICKER}&interval=1min&apikey={API_KEY}&outputsize=1"

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

def fetch_stock_data():
    response = requests.get(URL)
    data = response.json()
    if "values" in data:
        latest = data["values"][0]
        stock_info = {
            "ticker": TICKER,
            "price": round(float(latest["close"]), 2),
            "volume": int(latest.get("volume", 0)),
            "timestamp": latest["datetime"]
        }
        return stock_info
    return None

while True:
    stock_data = fetch_stock_data()
    if stock_data:
        producer.send("stock_prices", stock_data)
        print(f"Sent: {stock_data}")
    time.sleep(60)  # Fetch data every minute
