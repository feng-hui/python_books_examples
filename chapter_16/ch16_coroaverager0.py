#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/24 20:55


def averager():
    """
    execute at terminal
    example:
    from chapter_16.ch16_coroaverager0 import averager
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10) -> 10.0
    coro_avg.send(30) -> 20.0
    coro_avg.send(5) -> 15.0
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
