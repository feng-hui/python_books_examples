#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/6/10 19:53


def url_print(protocol, host, domain):
    """
    14_01
    :param protocol:
    :param host:
    :param domain:
    :return:
    """
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)


def func(x):
    """
    14_02
    :param x:
    :return:
    """
    print(x)
    return x


def dow_prices():
    """
    14_02 example.py
    :return:
    """
    res = {
        'IBM': 91.1,
        'AA': 13.25,
        'MSFT': 27.72
    }
    return res
