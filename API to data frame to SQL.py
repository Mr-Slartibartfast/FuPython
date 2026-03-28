import requests
import pandas as pd
import pyodbc

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data['rates'].items(), columns=['Currency', 'Rate'])

conn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=localhost;DATABASE=TrackDB;Trusted_Connection=yes;"
)
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO ExchangeRates (Currency, Rate)
        VALUES (?, ?)
    """, row['Currency'], row['Rate'])

conn.commit()
conn.close()