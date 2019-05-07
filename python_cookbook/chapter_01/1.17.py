#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/5/7 19:01
# 1.17 如何从字典中提取子集？
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print({key: value for key, value in prices.items() if value > 200})

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}

print({key: value for key, value in prices.items() if key in tech_names})
