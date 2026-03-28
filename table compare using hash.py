import hashlib

def hash_row(row):
    return hashlib.md5(str(row.values).encode()).hexdigest()

df1['hash'] = df1.apply(hash_row, axis=1)
df2['hash'] = df2.apply(hash_row, axis=1)

# Find differences
diff = df1[~df1['hash'].isin(df2['hash'])]

print("Rows in df1 not in df2:")
print(diff)