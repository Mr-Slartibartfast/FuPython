import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"{url} is UP (Status: {response.status_code})")
    except requests.exceptions.RequestException:
        print(f"{url} is DOWN")

# Example usage
check_website("https://www.google.com")