#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/5/4 19:53
# 过滤工具compress，它以一个iterable对象和一个相对应的Boolean选择器序列作为输入参数
# 然后输出iterable中对应选择器为True的元素
from itertools import compress

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(more5)
result = list(compress(addresses, more5))
print(result)
