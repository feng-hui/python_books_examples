#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/6 18:20
import asyncio
import aiohttp
from chapter_17.ch17_flags import main, show, save_flag, get_flag


@asyncio.coroutine
def get_one(url):
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
    resp = yield from aiohttp.request('GET', url, headers=headers)
    image = yield from resp.read_and_close()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_one(cc)
    file_name = cc.split('/')[-1]
    show(file_name)
    save_flag(image, file_name)
    return cc


def download_many(url_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(url_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == "__main__":
    f_n = __file__.split('/')[-1]
    print('>>>>>> [{}] Start scrawling page...'.format(f_n))
    img_urls = get_flag()
    print('>>>>>> [{}] Start downloading pictures by asyncio...'.format(f_n))
    main(download_many, img_urls)
    print('>>>>>> [{}] Download End...'.format(f_n))
