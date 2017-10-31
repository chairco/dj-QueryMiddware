import asyncio

import aiohttp

from edc import BASE_URL, show, main


@asyncio.coroutine
def get_glass_history(glass_id):
     url = '{}={glass_id}'.format(BASE_URL, glass_id=glass_id)
     #resp = yield from aiohttp.request('GET', url)
     with aiohttp.ClientSession() as session:
        resp = yield from session.get(url)     
        data = yield from resp.text()
        return len(data)


@asyncio.coroutine
def get_one(glass_id):
    data = yield from get_glass_history(glass_id)
    show(glass_id, data)
    return glass_id


def get_many(glass_list):
    loop = asyncio.get_event_loop()
    to_do = [get_one(glassid) for glassid in sorted(glass_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


if __name__ == '__main__':
    main(get_many)