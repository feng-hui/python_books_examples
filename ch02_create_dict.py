#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-2-27 下午7:31
# @author : Feng_Hui
# @email  : capricorn1203@126.com

a = dict(one=1, two=2)
print(a, type(a))

b = dict({'one': 1, 'two': 2})
print(b, type(b))

c = dict([('one', 1), ('two', 2)])
print(c, type(c))

d = dict(zip(['one', 'two'], [1, 2]))  # 字典推导
print(d, type(d))

e = {'one': 1, 'two': 2}
print(e, type(e))

# 判断值是否相等
print(a == b == c == d == e)

# 判断是否为同一个标识符
print(id(a) == id(b) == id(c) == id(d) == id(e))
