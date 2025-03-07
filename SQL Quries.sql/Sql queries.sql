CREATE DATABASE StockMarket;

USE StockMarket;
CREATE TABLE StockPrices (
    id INT IDENTITY(1,1) PRIMARY KEY,
    ticker NVARCHAR(10),
    price DECIMAL(10,2),
    volume BIGINT,
    timestamp DATETIME DEFAULT GETDATE()
)

#Moving Average


USE StockMarket;
SELECT
    timestamp,
    price,
    AVG(price) OVER (
        ORDER BY timestamp
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg
FROM StockPrices;

#Calculating the 20 days moving average of Tesla stock

USE StockMarket;
select timestamp,price,
avg(price) over (partition by ticker
order by timestamp rows 20 preceding ) as average_price_20
from Stockprices
where ticker = 'TSLA' and         
year(timestamp) = 2021;

#the average_price_20 column is only taking the average between the first row until the current row in the output, as per our project we need the good and price prices in stock so 
# we are calculating it between the years


USE StockMarket;
select timestamp,price,average_price_20
from(
select timestamp,price, 
avg(price) over (partition by ticker order by cast(timestamp as date) rows 20 preceding) as average_price_20 from StockPrices
where ticker = 'TSLA' and 
cast(timestamp as date) between '2021-01-01' and '2022-03-03')  as i
where year(i.timestamp) = 2022;



#Moving averages with a different time interval are good indicators to look to see whether the stock is bullish or bearish. 
#If we have 20 days moving average and 100 days moving average for Tesla (TSLA)
USE StockMarket;
SELECT txn_date, price,
    ROUND(average_price_20, 2) AS average_price_20,
    ROUND(ma100, 2) AS ma100,
    CASE 
        WHEN average_price_20 > ma100 THEN 'Bullish' 
        ELSE 'Bearish' 
    END AS bullish_indicator
FROM (
    SELECT 
        CAST(timestamp AS date) AS txn_date,  
        price,
        AVG(price) OVER (PARTITION BY ticker ORDER BY CAST(timestamp AS date) ROWS 20 PRECEDING) AS average_price_20,
        AVG(price) OVER (PARTITION BY ticker ORDER BY CAST(timestamp AS date) ROWS 100 PRECEDING) AS ma100
    FROM StockPrices 
    WHERE ticker = 'TSLA' AND YEAR(timestamp) BETWEEN 2021 AND 2022 
) AS i
WHERE YEAR(i.txn_date) = 2021; 
