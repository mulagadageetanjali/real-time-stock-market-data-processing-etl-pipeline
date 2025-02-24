import pyodbc

# Define the connection string
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"  # Adjust based on your setup
    "DATABASE=StockMarket;"
    "Trusted_Connection=yes;"
)

print("Microsoft SQL Server Connection Successful!")
conn.close()
