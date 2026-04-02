import pandas as pd
import hashlib

def hash_row(row):
    return hashlib.md5("".join(map(str, row)).encode()).hexdigest()

def compare_tables(df1, df2):
    df1['hash'] = df1.apply(hash_row, axis=1)
    df2['hash'] = df2.apply(hash_row, axis=1)

    diff = df1[~df1['hash'].isin(df2['hash'])]
    return diff

df1 = pd.read_csv("table1.csv")
df2 = pd.read_csv("table2.csv")

differences = compare_tables(df1, df2)
print(differences)