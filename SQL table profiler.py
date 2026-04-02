import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=localhost;DATABASE=YourDB;Trusted_Connection=yes;"
)

query = "SELECT * FROM your_table"
df = pd.read_sql(query, conn)

profile = pd.DataFrame({
    "column": df.columns,
    "dtype": df.dtypes,
    "nulls": df.isnull().sum(),
    "unique": df.nunique(),
    "min": df.min(numeric_only=True),
    "max": df.max(numeric_only=True)
})

print(profile)