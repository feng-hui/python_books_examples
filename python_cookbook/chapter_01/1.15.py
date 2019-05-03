#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/4/30 19:48
# 通过某个字段将记录分组
# groupby的使用

"""
注意：
在使用groupby方法之前，一个非常重要的步骤就是根据指定的字段将数据排序，因为它只检查连续的元素

原理：
groupby()函数扫描整个序列并查找连续相同值。在每次迭代的时候，它会返回一个值和一个迭代器对象，这个迭代器
对象可以生成元素值全部等于上面那个值的组中的所有对象。
"""
from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 通过groupby()方法
rows.sort(key=itemgetter('date'))
for date, item in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in item:
        print(i)

# 通过defaultdict
print('----------------------another method-------------------------')
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
for date, items in rows_by_date.items():
    print(date)
    for i in items:
        print(i)
