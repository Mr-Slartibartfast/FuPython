import os

def find_large_files(directory, size_limit_mb=100):
    size_limit = size_limit_mb * 1024 * 1024
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                if os.path.getsize(path) > size_limit:
                    print(f"{path} - {os.path.getsize(path) / (1024*1024):.2f} MB")
            except Exception:
                pass

# Example usage
find_large_files("C:/")  # Change to your path