#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

symbols = '$ASDasasassddsdd'

start_time = time.time()

beyond_ascii = [ord(s) for s in symbols if ord(s) > 60]

print(beyond_ascii, time.time() - start_time)

start_time2 = time.time()

beyond_ascii2 = filter(lambda c: c > 60, map(lambda c: ord(c), symbols))

print(beyond_ascii2, time.time() - start_time2)