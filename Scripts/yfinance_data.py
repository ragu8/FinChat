#yfinance_data.py


import yfinance as yf
import pandas as pd
import time 

def yfinance_data(ticker, start_date='2023-01-01', end_date=time.strftime('%Y-%m-%d')):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        filename = f"{ticker}_data.csv"
        data.to_csv(filename, mode='w', index=True)
        print("Data saved to", filename)
        return data
    
    except Exception as e:
        print("Error fetching data:", e)
        return None


if __name__ == "__main__":
    
    ticker = 'AAPL'
    
    stock_data = yfinance_data(ticker)
    
    if stock_data is not None:
        print(stock_data.head())
    else:
        print("Failed to fetch data.")

