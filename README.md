
# Real-time-Stock-Market-Data-Processing-ETL-Pipeline-
Extract: Stock data from a free API (Yahoo Finance, Alpha Vantage, IEX Cloud) Transform: Compute moving averages, detect trends, remove outliers Load: Store in a MongoDB/PostgreSQL database for analytics




+ Step 1: Install Python and Required Packages
  
✅ Check Python Version


Ensure you have Python 3.8 or later installed:
*****python --version*****

If it is not installed, please download it from official site.

+ Step 2: Install Dependencies
  
✅ Install all required Python libraries


*****pip install yfinance pandas pymongo psycopg2 kafka-python*****
What These Libraries Do?

yfinance → Fetches real-time stock data
pandas → Data transformation
pymongo → Connects to MongoDB
psycopg2 → Connects to PostgreSQL
kafka-python → Enables streaming 


![image](https://github.com/user-attachments/assets/763a69df-1ca4-4434-b66f-a05f8c87348b)
