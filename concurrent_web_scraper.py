import asyncio
import aiohttp
from bs4 import BeautifulSoup

URLS = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]

SEM = asyncio.Semaphore(5)  # limit concurrency

async def fetch(session, url):
    async with SEM:
        async with session.get(url) as response:
            return await response.text()

async def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.string if soup.title else "No title"

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        pages = await asyncio.gather(*tasks)

        results = await asyncio.gather(*[parse(p) for p in pages])
        for url, title in zip(URLS, results):
            print(f"{url}: {title}")

asyncio.run(main())