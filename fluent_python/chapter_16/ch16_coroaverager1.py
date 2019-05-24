#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/24 21:51
from chapter_16.ch16_coroutil import coroutine


@coroutine
def averager():
    """
    经过预激协程装饰器装饰之后的计算平均值
    使用方法：
    #     >>> from chapter_16.ch16_coroaverager0 import averager
    #     >>> coro_avg = averager()
    #     >>> coro_avg.send(10) -> 10.0
    #     >>> coro_avg.send(30) -> 20.0
    #     >>> coro_avg.send(5) -> 15.0
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
