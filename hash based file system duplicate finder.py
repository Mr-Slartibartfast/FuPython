import os
import hashlib

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            try:
                h = file_hash(path)
                if h in hashes:
                    duplicates.append((path, hashes[h]))
                else:
                    hashes[h] = path
            except Exception as e:
                print(f"Error: {path} - {e}")

    return duplicates

dupes = find_duplicates("C:/data")
for d in dupes:
    print("Duplicate:", d)