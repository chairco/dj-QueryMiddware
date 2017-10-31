import os
import time
import sys

import requests


with open('sample_his.csv', 'r') as fp:
    gpairs = fp.readlines()

data_list = [i.rstrip().split(',') for i in gpairs]


BASE_URL = 'http://localhost:8000/autosearch/edcs/'


def get_glass_summary(glass_id, step_id, start_time):
    url = '{url}/?glassid={glassid}&stepid={stepid}&starttime={starttime}'.format(
        url=BASE_URL, glassid=glass_id, stepid=step_id, starttime=start_time
    )
    resp = requests.get(url)
    return resp.content


def show(text, data):
    print(text, data, end=' ')
    sys.stdout.flush()


def get_many(data_list):
    for gpairs in data_list:
        data = get_glass_summary(
            glass_id=gpairs[0],
            step_id=gpairs[1],
            start_time=gpairs[2]
        )
        show(gpairs[0], len(data))

    return data


def main(get_many):
    t0 = time.time()
    datas = get_many(data_list=data_list)
    elapsed = time.time() - t0
    msg = '\n{} glassid get in {:.2f}s'
    print(msg.format(len(datas), elapsed))
    return datas


if __name__ == '__main__':
    main(get_many)
