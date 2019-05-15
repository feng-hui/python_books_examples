#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/5/15 19:37
"""
2.1 使用多个界定符分割字符串

问题：
你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。

解决方案：
string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有
多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，
最好使用 re.split() 方法。
"""
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'

# 01、不输出分隔符
res = re.split(r'[,;\s]\s*', line)
print(res)

# 02 使用捕获分组, 输出分隔符
fields = re.split(r'(,|;|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2]

# 输出值与分隔符的列表
print(values)
print(delimiters)

# 输出分割前的值
print(''.join(v + d for v, d in zip(values, delimiters)))

# 03、使用非捕获分组
print(re.split(r'(?:,|;|\s)\s*', line))
