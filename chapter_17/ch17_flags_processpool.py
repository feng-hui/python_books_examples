#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/22 17:57
from concurrent import futures
from chapter_17.ch17_flags import save_flag, main, get_flag, get_one, show


def download_one(url):
    img = get_one(url)
    file_name = url.split('/')[-1]
    show(file_name)
    save_flag(img, file_name)


def download_many(url_list):
    """
    use process pool
    """
    with futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, url_list)


if __name__ == "__main__":
    f_n = __file__.split('/')[-1]
    print('>>>>>> [{}] Start scrawling page...'.format(f_n))
    img_urls = get_flag()
    print('>>>>>> [{}] Start downloading pictures by process pool...'.format(f_n))
    main(download_many, img_urls)
    print('>>>>>> [{}] Download End...'.format(f_n))
