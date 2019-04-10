#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-22 21:55
# @author : feng_hui
# @email  : capricorn1203@126.com
# calculate 0+1+...+99
from functools import reduce
from operator import add


# method 1
print('the method1: use sum directly, the result is: ', sum(range(100)))

# method 2
print('the method 2: use function reduce and range, the result is: ', reduce(add, range(100)))