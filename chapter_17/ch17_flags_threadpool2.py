#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/2/27 11:02
from concurrent import futures
from chapter_17.ch17_flags import save_flag, main, get_flag, get_one, show
MAX_WORKERS = 20


def download_one(*args):
    url, default1, default2 = args[0]
    print('>>>>>>request url:{url}, default param1:{default1}, default param2:{default2}'.format(
        url=url,
        default1=default1,
        default2=default2
    ))
    img = get_one(url)
    file_name = url.split('/')[-1]
    show(file_name)
    save_flag(img, file_name)


def download_many(url_list):
    params = ((url, 'default1', 'default2') for url in url_list)
    workers = min(MAX_WORKERS, len(url_list))
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(download_one, params)


if __name__ == "__main__":
    # f_n = __file__.split('/')[-1]
    # print('>>>>>> [{}] Start scrawling page...'.format(f_n))
    # img_urls = get_flag()
    # print('>>>>>> [{}] Start downloading pictures by thread pool...'.format(f_n))
    # main(download_many, img_urls)
    # print('>>>>>> [{}] Download End...'.format(f_n))
    import re
    res = re.search('bi', 'bike')
    if res:
        print(res.end())
