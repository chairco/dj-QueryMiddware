import asyncio

import aiohttp

from edc import BASE_URL, show, main


#content = {}

@asyncio.coroutine
def get_glass_history(glass_id):
    url = '{}={glass_id}'.format(BASE_URL, glass_id=glass_id)
    # resp = yield from aiohttp.request('GET', url)
    with aiohttp.ClientSession() as session:
        resp = yield from session.get(url)
        data = yield from resp.text()

        return data


@asyncio.coroutine
def get_one(glass_id, semaphore):
    with (yield from semaphore):
        data = yield from get_glass_history(glass_id)
        show(glass_id, len(data))
        #content.setdefault(glass_id, data)

    return {glass_id: data}  # data return type


@asyncio.coroutine
def quote_many(glass_list, conn_limit=20):
    semaphore = asyncio.Semaphore(conn_limit)
    coroutines = [get_one(glassid, semaphore)
                  for glassid in sorted(glass_list)]
    quotes = yield from asyncio.gather(*coroutines)
    return quotes


def get_many(glass_list):
    loop = asyncio.get_event_loop()
    #to_do = [get_one(glassid) for glassid in sorted(glass_list)]
    #wait_coro = asyncio.wait(to_do)
    #res, _ = loop.run_until_complete(wait_coro)
    quotes = loop.run_until_complete(
        quote_many(glass_list=glass_list, conn_limit=100))
    loop.close()
    return quotes


if __name__ == '__main__':
    main(get_many)
