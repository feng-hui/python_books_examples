#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/10 19:07
import os
import sys
import string
import argparse
import requests
from lxml.html import etree
import time
from enum import Enum
from collections import namedtuple

Result = namedtuple('Result', 'status data')


class HTTPStatus(Enum):
    ok = 1
    not_found = 2
    error = 3


POP20_CC = 'ai'.split()

DOWNLOAD_DIR = 'E:\\wksp\\fluent_python_examples\\chapter_17\\download'  # download dir

DEFAULT_CONCURRENT = 1  # default concurrent requests
MAX_CONCURRENT = 1  # max concurrent requests

COUNTRY_CODES_FILE = 'country.txt'  # country codes file for all cc

BASE_URL = 'https://www.jikexueyuan.com/course/{}/'

A_Z = string.ascii_uppercase  # 26 capital letters


def get_urls_list(url):
    """get all urls in the page"""
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
    content = requests.get(url, headers=headers).text
    html = etree.HTML(content)
    images_urls = html.xpath('//img[@class="lessonimg"]/@src')
    return images_urls


def save(img, file_name):
    """
    save flags
    :param img: flag image content
    :param file_name: flag image name
    :return:
    """
    path = os.path.join(DOWNLOAD_DIR, file_name)
    print(path)
    with open(path, 'wb') as f:
        f.write(img)


def initial_report(cc_list, actual_req):
    """
    print initial report when downloading flags
    :param cc_list: cc list
    :param actual_req: actual req numbers
    # :param server_label: server label of the SERVERS
    :return: None
    """
    if len(cc_list) <= 10:
        cc_msg = ', '.join(cc_list)
    else:
        cc_msg = 'from {} to {}'.format(cc_list[0], cc_list[-1])
    # print('{} site: {}'.format(server_label, SERVERS[server_label]))
    msg = 'Searching for {} flag{}: {}'
    plural = 's' if len(cc_list) > 1 else ''
    print(msg.format(len(cc_list), plural, cc_msg))
    plural = 's' if actual_req > 1 else ''
    msg = '{} concurrent connection{} will be used.'
    print(msg.format(actual_req, plural))


def final_report(counter, start_time):
    """
    final report
    :param counter: counter object
    :param start_time: start time
    :return:None
    """
    elapsed = time.time() - start_time
    print('-' * 20)
    msg = '{} flag{} download.'
    plural = 's' if counter[HTTPStatus.ok] > 1 else ''
    print(msg.format(counter[HTTPStatus.ok], plural))

    if counter[HTTPStatus.not_found]:
        print(counter[HTTPStatus.not_found], 'not found')

    if counter[HTTPStatus.error]:
        plural = 's' if counter[HTTPStatus.error] > 1 else ''
        print('{} error{}.'.format(counter[HTTPStatus.error], plural))

    print('Elapsed time: {:.2f}s'.format(elapsed))


def expand_cc_args(every_cc, all_cc, cc_args, limit):
    """
    :param every_cc: get_flags from AA...ZZ
    :param all_cc: get all flags (AD TO Zw)
    :param cc_args: country or 1st letter
    :param limit: limit number
    :return:
    """
    codes = set()
    if every_cc:
        codes.update(a+b for a in A_Z for b in A_Z)
    elif all_cc:
        with open(COUNTRY_CODES_FILE) as fp:
            text = fp.read()
        codes.update(text.split())
    else:
        for cc in (c.upper() for c in cc_args):
            if len(cc) == 1 and cc in A_Z:
                codes.update(cc+c for c in A_Z)
            elif len(cc) == 2 and all(c in A_Z for c in cc):
                codes.add(cc)
            else:
                msg = 'each CC argument must be A TO Z or AA to ZZ'
                raise ValueError('*** Usage error: ' + msg)
    return sorted(codes)[:limit]


def expand_cc_args2(every_cc, all_cc, cc_args, limit):
    """
    :param every_cc:
    :param all_cc:
    :param cc_args:
    :param limit:
    :return:
    """
    codes = set()
    if every_cc or all_cc:
        codes = codes
    elif cc_args:
        for cc in cc_args:
            if cc in POP20_CC:
                codes.add(BASE_URL.format(cc))
    else:
        msg = 'each CC argument must be A TO Z or AA to ZZ'
        raise ValueError('*** Usage error: ' + msg)
    return sorted(codes)[:limit]


def process_args(default_concur_req):
    # server_options = ', '.join(sorted(SERVERS))
    parser = argparse.ArgumentParser(description='Download flags for country codes.'
                                                 'Default: top 20 countries by population')
    parser.add_argument('cc', metavar='CC', nargs='*',
                        help='country code or 1st letter (eg. B for BA...BZ)')
    parser.add_argument('-a', '--all', action='store_true',
                        help='get all available flags (AD to ZW)')
    parser.add_argument('-e', '--every', action='store_true',
                        help='get flags for every possible code (AA...ZZ)')
    parser.add_argument('-l', '--limit', metavar='N', type=int,
                        help='limit to N first codes', default=sys.maxsize)
    parser.add_argument('-m', '--max_req', metavar='CONCURRENT', type=int,
                        default=default_concur_req,
                        help='maximum concurrent_requests (default={})'
                             .format(default_concur_req))
    # parser.add_argument('-s', '--server', metavar='LABEL',
    #                     default=DEFAULT_SERVER,
    #                     help='Server to hit; one of {} (default={})'
    #                          .format(server_options, DEFAULT_SERVER))
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='output detailed progress info')

    args = parser.parse_args()
    if args.max_req < 1:
        print('*** Usage Error: --max_req CONCURRENT must be >= 1')
        print(parser.print_usage())
        sys.exit(1)
    if args.limit < 1:
        print('*** Usage Error: --limit N must be >= 1')
        print(parser.print_usage())
        sys.exit(1)

    try:
        cc_list = expand_cc_args2(args.every, args.all, args.cc, args.limit)
    except ValueError as exc:
        print(exc.args[0])
        print(parser.print_usage())
        sys.exit(1)

    if not cc_list:
        cc_list = sorted([BASE_URL.format(cc) for cc in POP20_CC])

    return args, cc_list


def main(download_many, default_concur_req, max_concur_erq):
    args, cc_list = process_args(default_concur_req)
    cc_list = get_urls_list(cc_list[0])
    actual_req = min(default_concur_req, max_concur_erq, len(cc_list))
    initial_report(cc_list, actual_req)
    # base_url = SERVERS[args.server]
    t0 = time.time()
    counter = download_many(cc_list, args.verbose, actual_req)
    assert sum(counter.values()) == len(cc_list), \
        'some download are unaccounted for'
    final_report(counter, t0)
