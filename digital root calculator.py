def digital_root(s):
    total = sum(int(c) for c in s if c.isdigit())
    
    while total > 9:
        total = sum(int(c) for c in str(total))
    
    return total

print(digital_root("abc123xyz"))