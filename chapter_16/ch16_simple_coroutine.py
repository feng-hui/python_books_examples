#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/22 11:28


def simple_coroutine():
    """
    最简单的生成器
    :return:
    """
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)
