#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/28 19:42
from collections import namedtuple

Result = namedtuple('Result', 'count, average')


def averager():
    """
    execute at terminal
    example:
    from chapter_16.ch16_coroaverager0 import averager
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(5)
    coro_avf.send(None) -> exception(StopIteration)

    You can catch the exception through the following code at the terminal.
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)
