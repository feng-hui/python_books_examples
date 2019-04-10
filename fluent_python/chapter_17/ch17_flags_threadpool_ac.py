#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/22 17:15
from concurrent import futures
from chapter_17.ch17_flags import save_flag, main, get_flag, get_one, show


def download_one(url):
    img = get_one(url)
    file_name = url.split('/')[-1]
    show(file_name)
    save_flag(img, file_name)
    return file_name


def download_many(url_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        todo = []
        for each_url in url_list[:5]:
            future = executor.submit(download_one, each_url)
            todo.append(future)
            msg = 'Schedule {}:{}'
            print(msg.format(each_url.split('/')[-1], future))

        results = []
        for future in futures.as_completed(todo):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    # print(len(results))
    return len(results)


if __name__ == "__main__":
    f_n = __file__.split('/')[-1]
    print('>>>>>> [{}] Start scrawling page...'.format(f_n))
    img_urls = get_flag()
    print('>>>>>> [{}] Start downloading pictures by thread pool ac...'.format(f_n))
    main(download_many, img_urls)
    print('>>>>>> [{}] Download End...'.format(f_n))
