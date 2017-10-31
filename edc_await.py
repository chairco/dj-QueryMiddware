import asyncio

import aiohttp

from edc import BASE_URL, show, main

from itertools import chain

#content = {}


async def get_glass_history(glass_id):
    url = '{}={glass_id}'.format(BASE_URL, glass_id=glass_id)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #data = await resp.text()
            data = await resp.json()

    return data


async def get_one(glass_id, semaphore):
    with (await semaphore):
        data = await get_glass_history(glass_id)
        show(glass_id, len(data))
        #content.setdefault(glass_id, data)
    
    return {glass_id: data} # data return type


async def quote_many(glass_list, conn_limit=20):
    semaphore = asyncio.Semaphore(conn_limit)
    coroutines = [get_one(glassid, semaphore) for glassid in sorted(glass_list)]
    quotes = await asyncio.gather(*coroutines)

    return quotes


def get_many(glass_list):
    loop = asyncio.get_event_loop()
    #to_do = [get_one(glassid) for glassid in sorted(glass_list)]
    #wait_coro = asyncio.wait(to_do)
    #res, _ = loop.run_until_complete(wait_coro)
    conn_limit = min(len(glass_list), 80)
    quotes = loop.run_until_complete(quote_many(glass_list=glass_list, conn_limit=conn_limit))
    loop.close()

    return quotes


def report(result):
    with open('sample_his.csv', 'w') as fp:
        for data in result:
            for d in chain.from_iterable(data.values()):
                fp.write(
                    '{},{},{}\n'.format(
                        d['GLASS_ID'],
                        d['STEP_ID'],
                        d['GLASS_START_TIME']
                    )
                )


if __name__ == '__main__':
    result = main(get_many)
    report(result=result)