#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/21 19:16
import datetime
import os
import sys
import time

import requests
from requests.exceptions import ConnectTimeout
from lxml import etree

BASE_URL = 'https://www.jikexueyuan.com/course/mobile/'

DOWNLOAD_DIR = 'E:\\wksp\\fluent_python_examples\\chapter_17\\download'


def save_flag(img, file_name):
    path = os.path.join(DOWNLOAD_DIR, file_name)

    with open(path, 'wb') as f:
        f.write(img)


def get_flag():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.jikexueyuan.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    content = requests.get(BASE_URL, headers=headers).text
    html = etree.HTML(content)
    images_urls = html.xpath('//img[@class="lessonimg"]/@src')
    return images_urls


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
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        return resp.content
    except ConnectTimeout:
        raise Exception('ConnectionTimeout,Please retry after a few minutes.')


def show(text):
    print('>>>>>>downloading pictures:{}'.format(text), end='\n')
    sys.stdout.flush()


def download_many(url_list):
    for each_image_url in url_list:
        img = get_one(each_image_url)
        file_name = each_image_url.split('/')[-1]
        show(file_name)
        save_flag(img, file_name)


def main(down_func, url_list):
    t0 = time.time()
    down_func(url_list)
    elapsed = time.time() - t0
    msg = '>>>>>> Download all images in {:.2f}s.'
    print(msg.format(elapsed))


if __name__ == "__main__":
    f_n = __file__.split('/')[-1]
    print('>>>>>> [{}] Start scrawling page...'.format(f_n))
    img_urls = get_flag()
    print('>>>>>> [{}] Start downloading pictures by single thread...'.format(f_n))
    main(download_many, img_urls)
    print('>>>>>> [{}] Download End...'.format(f_n))
