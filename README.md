# Real-time-Stock-Market-Data-Processing-ETL-Pipeline-
***Extract:*** Stock data from a free API (Yahoo Finance, Alpha Vantage, IEX Cloud) 


***Transform:*** Compute moving averages, detect trends, remove outliers 


***Load:*** Store in a MongoDB/PostgreSQL database for analytics


## Step 1: Install Python and Required Packages
  
Check Python Version


Ensure you have Python 3.8 or later installed:
*****python --version*****

If it is not installed, please download it from official site.

## Step 2: Install Dependencies
  
Install all required Python libraries


*****pip install yfinance pandas pymongo psycopg2 kafka-python*****
What These Libraries Do?

yfinance → Fetches real-time stock data
pandas → Data transformation
pymongo → Connects to MongoDB
psycopg2 → Connects to PostgreSQL
kafka-python → Enables streaming 


![image](https://github.com/user-attachments/assets/763a69df-1ca4-4434-b66f-a05f8c87348b)




## Step 3: Install & Configure Apache Kafka (Free Streaming)
Download & Set Up Kafka Locally
Download Kafka:
Extract the downloaded file.
Open a terminal and start Zookeeper (Kafka dependency):
Start Kafka Server
Create a Kafka topic for stock data:
Here the topic created was stockprices



## Step 4:Create the Database & Table:
Open SQL Server Management Studio (SSMS)
Connect to (local)\SQLEXPRESS
Run this SQL query to create a StockMarket database:
CREATE DATABASE StockMarket;
**Use the database and create a StockPrices table;**

**USE StockMarket;**

**CREATE TABLE StockPrices (**
    **id INT IDENTITY(1,1) PRIMARY KEY,**
    **ticker NVARCHAR(10),**
    **price DECIMAL(10,2),**
    **volume BIGINT,**
    **timestamp DATETIME DEFAULT GETDATE()**
**);**


## Step 5:Extract Live Stock Data


## Step 6:Consume & Store Data in SQL Server


## Step 7:Query & Analyze Data