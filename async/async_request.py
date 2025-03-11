import aiohttp
import asyncio
import time

async def fetch_page(url):
    page_start = asyncio.get_running_loop().time()  # ✅ Use asyncio time
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {asyncio.get_running_loop().time() - page_start:.2f} seconds')
            return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page) 
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks            

async def main():
    tasks = [fetch_page('http://google.com') for _ in range(50)]
    start = asyncio.get_running_loop().time()
    await asyncio.gather(*tasks)
    print(f'it took {asyncio.get_running_loop().time() - start:.2f} seconds')

asyncio.run(main())  # ✅ Modern asyncio execution
