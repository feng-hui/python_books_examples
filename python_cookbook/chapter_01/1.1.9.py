#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/5/11 18:04
"""
1.19 转换并同时计算数据

问题：
你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ），但是首先你需要先转换或者过滤数据

解决方案：
一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。

例如：
nums = [1, 2, 3, 4, 5]
s = sum(x for x in nums)
"""
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
max_shares = max(s['shares'] for s in portfolio)
print(min_shares, max_shares)

min_shares = min(portfolio, key=lambda s: s['shares'])
sorted_shares = sorted(portfolio, key=lambda s: s['shares'])
print(min_shares, sorted_shares)
