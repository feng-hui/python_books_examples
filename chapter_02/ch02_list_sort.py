#!/usr/bin/python
# -*- coding: utf-8 -*-

"""list.sort()和sorted的使用方法"""

fruits = ['grape', 'raspberry', 'apple', 'banana']

print('the result of using sorted: ', sorted(fruits))

print('default list: ', fruits)

print('change the ascend to descend through using sorted: ', sorted(fruits, reverse=True))

print('sorted by the length of string using sorted: ', sorted(fruits, key=len))

print('default list: ', fruits)

print('the result of using list.sort: ', list.sort(fruits))

print('default list: ', fruits)