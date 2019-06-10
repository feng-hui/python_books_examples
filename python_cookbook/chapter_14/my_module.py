#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/6/10 19:53


def url_print(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)
