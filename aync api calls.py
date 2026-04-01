import asyncio
import aiohttp
import pandas as pd

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, API_URL) for _ in range(10)]  # simulate multiple pulls
        results = await asyncio.gather(*tasks)

    df = pd.json_normalize(results)
    print(df.head())

asyncio.run(main())