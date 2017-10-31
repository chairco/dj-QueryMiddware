import os
import time
import sys

import requests

with open('sample-300.csv', 'r') as fp:
    glass_id = fp.readlines()

glass_id = [i.rstrip() for i in glass_id]

glass_list = glass_id[:100]


BASE_URL = 'http://localhost:8000/autosearch/edch/?glassid'


def get_glass_history(glass_id):
    url = '{}={glass_id}'.format(BASE_URL, glass_id=glass_id)
    resp = requests.get(url)
    return resp.content


def show(text, data):
    print(text, data, end=' ')
    sys.stdout.flush()


def get_many(glass_list):
    for glassid in sorted(glass_list):
        data = get_glass_history(glassid)
        show(glassid, len(data))

    return len(glass_list)


def main(get_many):
    print('Total: {}'.format(len(glass_list)))
    t0 = time.time()
    count = get_many(glass_list=glass_list)
    elapsed = time.time() - t0
    msg = '\n{} glassid get in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(get_many)