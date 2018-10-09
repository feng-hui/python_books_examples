#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-8 下午9:45
# @author : Feng_Hui
# @email  : capricorn1203@126.com
import builtins
from collections import OrderedDict, Counter, ChainMap

# how to use OrderedDict
ordered_dict = OrderedDict()
ordered_dict.update([('a', 2), ('b', 3)])
print(ordered_dict)
print(ordered_dict.popitem())  # pop the last one
print(ordered_dict.popitem(last=False))  # pop the first one

# how to use ChainMap
# print('>>>>>>locals()>>>>>>\n', locals())
# print('>>>>>>globals()>>>>>>\n', globals())
# print('>>>>>>builtins()>>>>>>\n', builtins)
py_lookup = ChainMap(locals(), globals(), vars(builtins))
print(py_lookup)


# how to use Counter
ct = Counter('abracadabra')
print(ct, ct.get('a'))  # 可以计算字符串(可迭代对象)中字符出现的次数
ct.update('aaaaazzz')
print(ct.most_common(3))  # 返回映射中最常见的n个键和它们的计数

ct2 = Counter(['a', 'b', 'a'])
print(ct2)
