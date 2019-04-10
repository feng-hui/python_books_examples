#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-22 21:40
# @author : feng_hui
# @email  : capricorn1203@126.com
# the difference of map filter and listcomps
# calculate factorial


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == "__main__":
    print(list(map(factorial, range(10))))
    print([factorial(n) for n in range(10)])
    print(list(map(factorial, filter(lambda n: n % 2, range(10)))))
    print([factorial(n) for n in range(10) if n % 2])
