import pyodbc
import json
from kafka import KafkaConsumer

# SQL Server Connection
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=StockMarket;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    "stock_prices",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

def insert_data_to_sqlserver(data):
    query = "INSERT INTO StockPrices (ticker, price, volume,timestamp) VALUES (?, ?, ?,?)"
    cursor.execute(query, (data["ticker"], data["price"], data["volume"],data["timestamp"]))
    conn.commit()
    print(f"Inserted into SQL Server: {data}")

# Consume data from Kafka & insert into SQL Server
for message in consumer:
    stock_data = message.value
    
    # Check if the record already exists
    cursor.execute("SELECT COUNT(*) FROM StockData WHERE ticker=? AND timestamp=?", 
                   (stock_data["ticker"], stock_data["timestamp"]))
    exists = cursor.fetchone()[0]

    if exists == 0:  # Only insert if it doesn't exist
        insert_data_to_sqlserver(stock_data)
        print("Inserted into SQL Server")
    else:
        print("Duplicate detected, skipping")
