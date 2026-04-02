import pandas as pd
import pyodbc

# 🔧 CONFIG
server = ".\\SQLEXPRESS"  # Local SQL Express instance
database = "WorldEconomicData"
table = "dbo.world_economic_data"

def profile_table(server, database, table):
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, conn)

    profile = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.astype(str),
        "null_count": df.isnull().sum(),
        "null_pct": (df.isnull().mean() * 100).round(2),
        "unique_count": df.nunique(),
    })

    # Add numeric stats safely
    numeric_df = df.select_dtypes(include='number')

    if not numeric_df.empty:
        stats = numeric_df.agg(['min', 'max', 'mean', 'std']).T
        stats.columns = ['min', 'max', 'mean', 'std']
        profile = profile.merge(stats, left_on="column", right_index=True, how="left")

    return profile




result = profile_table(server, database, table)

print(result)