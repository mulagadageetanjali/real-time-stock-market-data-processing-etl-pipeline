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
    query = "INSERT INTO StockPrices (ticker, price, volume) VALUES (?, ?, ?)"
    cursor.execute(query, (data["ticker"], data["price"], data["volume"]))
    conn.commit()
    print(f"Inserted into SQL Server: {data}")

# Consume data from Kafka & insert into SQL Server
for message in consumer:
    stock_data = message.value
    insert_data_to_sqlserver(stock_data)
