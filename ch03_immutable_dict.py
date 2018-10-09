#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-9 下午8:53
# @author : Feng_Hui
# @email  : capricorn1203@126.com
# The value of d_proxy will be changed when you update the original dict(d).
# the value of d_pxoxy is dynamic
from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print('d: ', d)
print('d_proxy: ', d_proxy)

print('d[1]: ', d[1])
print('d_proxy: ', d_proxy[1])

try:
    d_proxy[2] = 'B'
except TypeError:
    print(TypeError)

d[2] = 'B'
print('new d: ', d)
print('new d_proxy: ', d_proxy)
