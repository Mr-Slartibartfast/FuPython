import requests
import beautifulsoup4 as bs4
from bs4 import BeautifulSoup

# Step 1: Fetch the page
url = "https://example.com"
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract data
headlines = soup.find_all("h2")

# Step 4: Print results
for h in headlines:
    print(h.get_text(strip=True))