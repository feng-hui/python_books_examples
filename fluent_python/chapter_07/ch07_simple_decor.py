#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-26 21:33
# @author : feng_hui
# @email  : capricorn1203@126.com
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ''.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
