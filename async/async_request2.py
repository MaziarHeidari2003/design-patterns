


import aiohttp
import asyncio
import time
import async_timeout

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url)) 
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks            


async def fetch_page(session,url):
    page_start = asyncio.get_running_loop().time()  # ✅ Use asyncio time
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
                print(f'Page took {asyncio.get_running_loop().time() - page_start:.2f} seconds')
                return response.status

async def get_multiple_pages(loop,*urls):
    tasks = []
    async with  aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks) 
        return await grouped_tasks   

loop = asyncio.get_event_loop() 

urls = ['http://google.com' for _ in range(50)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop,*urls))
print(f'it took {time.time() - start:.2f} seconds')

