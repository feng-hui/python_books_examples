#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-24 21:32
# @author : feng_hui
# @email  : capricorn1203@126.com


class C(object):
    pass


obj = C()


def func(): pass


# 获取函数有而对象没有的所有属性
print(sorted(set(dir(func)) - set(dir(obj))))
