import hashlib

def guid_to_int64(guid: str) -> int:
    h = hashlib.sha256(guid.encode('utf-8')).digest()
    return int.from_bytes(h[:8], 'big', signed=False)

guid = "123e4567-e89b-12d3-a456-426614174000"
print(guid_to_int64(guid))


import xxhash

def guid_to_int64_fast(guid: str) -> int:
    return xxhash.xxh64(guid).intdigest()