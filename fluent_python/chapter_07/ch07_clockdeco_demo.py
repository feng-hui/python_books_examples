#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-26 21:38
# @author : feng_hui
# @email  : capricorn1203@126.com
import time
from chapter_07.ch07_simple_decor import clock
from functools import lru_cache


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


@lru_cache()
@clock
def fibonacci2(n):
    return n if n < 2 else fibonacci2(n - 2) + fibonacci2(n - 1)


if __name__ == "__main__":
    # print('*' * 40, 'Calling snooze(.123)')
    # snooze(.123)
    # print('*' * 40, 'Calling factorial(6)')
    # factorial(6)
    # print('*' * 40, 'Calling fibonacci(6)')
    # fibonacci(6)
    fibonacci2(6)
