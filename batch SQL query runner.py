import pyodbc

queries = [
    "DELETE FROM Results WHERE Time IS NULL",
    "UPDATE Results SET Time = 0 WHERE Time < 0",
    "SELECT COUNT(*) FROM Results"
]

conn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=localhost;DATABASE=TrackDB;Trusted_Connection=yes;"
)
cursor = conn.cursor()

for q in queries:
    cursor.execute(q)
    try:
        print(cursor.fetchall())
    except:
        pass

conn.commit()
conn.close()