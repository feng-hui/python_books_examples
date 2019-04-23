#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/4/23 19:57
# 1.11 how to use named slice?（如何使用命名切片）
# 好处：减少硬编码切片下标

# 1、直接使用命名后的切片获取对应的值
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)  # 20 start 23 stop None step
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# 2、切片映射到一个确定大小的序列上
a = slice(5, 50, 2)
print(a.start, a.stop, a.step)
s = 'HelloWorld'
for i in range(*a.indices(len(s))):
    print(s[i])
