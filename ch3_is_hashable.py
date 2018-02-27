#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-2-27 下午7:22
# @author : Feng_Hui
# @email  : capricorn1203@126.com

tt = (1, 2, (30, 40))  # hashable
print(hash(tt))

try:
    tf = (1, 2, [30, 40])  # cannot hashable
    print(hash(tf))
except Exception as e:
    print(e)

tf = (1, 2, frozenset([30, 40]))  # hashable
print(hash(tf))
