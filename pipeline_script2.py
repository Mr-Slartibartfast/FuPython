
import pyodbc
import yfinance as yf
import pandas as pd
from datetime import datetime
import schedule
import time 


def get_stock_price(ticker="VFIFX"):
    stock = yf.Ticker(ticker)

    data = stock.history(period="1d")

    if data.empty:
        raise Exception("No data returned from Yahoo Finance")

    latest = data.iloc[-1]

    return {
        "ticker": ticker,
        "price": float(latest["Close"]),
        "date": datetime.now()
    }

if __name__ == "__main__":
    result = get_stock_price()
    print(result)

def insert_stock_price(data):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=SERVERNAME\\SQLEXPRESS;"
        "DATABASE=Stocks;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()

    query = """
    INSERT INTO StockPrices (Ticker, Price, PriceDate)
    VALUES (?, ?, ?)
    """

    cursor.execute(query, data["ticker"], data["price"], data["date"])

    conn.commit()
    cursor.close()
    conn.close()

# from extract_stock import get_stock_price
# from load_to_sql import insert_stock_price

def run_pipeline():
    data = get_stock_price("VFIFX")
    print(f"Pulled data: {data}")

    insert_stock_price(data)
    print("Inserted into SQL Server")

if __name__ == "__main__":
    run_pipeline()

