#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/24 10:35
import requests
import tqdm
from collections import Counter
from ch17_flags2_common import (BASE_URL, HTTPStatus, Result, save, main,
                                 DEFAULT_CONCURRENT, MAX_CONCURRENT)



def get_one(url, verbose=False):
    file_name = url.split('/')[-1]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'a1.jikexueyuan.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not found'
        else:
            raise
    else:
        save(resp.content, file_name)
        status = HTTPStatus.ok
        msg = 'ok'

    if verbose:
        print(file_name, msg)

    return Result(status, file_name)


def download_many(cc_list, verbose, max_req):
    counter = Counter()
    cc_iter = sorted(cc_list)

    if not verbose:
        cc_iter = tqdm.tqdm(cc_list)

    for cc in cc_iter:
        try:
            res = get_one(cc, verbose)
        except requests.exceptions.HTTPError as exc:
            error_msg = 'HTTP error {res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc:
            error_msg = 'Connection error'
        else:
            error_msg = ''
            status = res.status

        if error_msg:
            status = HTTPStatus.error

        counter[status] += 1

        if verbose and error_msg:
            print('*** Error for {}: {}'.format(cc, error_msg))

    return counter


if __name__ == "__main__":
    main(download_many, default_concur_req=DEFAULT_CONCURRENT, max_concur_erq=MAX_CONCURRENT)
