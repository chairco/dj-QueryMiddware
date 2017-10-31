import asyncio

import aiohttp

from edc import show

from itertools import chain

from edcs import BASE_URL, show, main

from dateutil.parser import parse



async def get_glass_summary(glass_id, step_id, start_time):
    url = '{url}?glassid={glassid}&stepid={stepid}&starttime={starttime}'.format(
        url=BASE_URL, glassid=glass_id, stepid=step_id, starttime=parse(start_time, ignoretz=True)
    )
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
    
    return data


async def get_one(glass_id, step_id, start_time, semaphore):
    with (await semaphore):
        data = await get_glass_summary(glass_id, step_id, start_time)
        show(glass_id, len(data))
    
    return data


async def quote_many(datas, conn_limit=20):
    semaphore = asyncio.Semaphore(conn_limit)
    coroutines = [
        get_one(
            data[0], 
            data[1], 
            data[2],
            semaphore
        ) for data in datas
    ]
    quotes = await asyncio.gather(*coroutines)
    return quotes


def get_many(data_list):
    loop = asyncio.get_event_loop()
    quotes = loop.run_until_complete(quote_many(datas=data_list, conn_limit=30))
    loop.close()
    return quotes


if __name__ == '__main__':
    main(get_many)