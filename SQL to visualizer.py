import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

conn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=localhost;DATABASE=TestDB;Trusted_Connection=yes;"
)

query = "SELECT date, value FROM MyTable"
df = pd.read_sql(query, conn)

plt.scatter(df['date'], df['value'])
plt.show()