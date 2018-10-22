#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-12 下午9:09
# @author : Feng_Hui
# @email  : capricorn1203@126.com
# how to use chainmap
# https://docs.python.org/3/library/collections.html#collections.ChainMap
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map, type(chain_map))
print(chain_map.get('a'))
print(chain_map.maps)  # mapping list
dict2['e'] = 5  # 更新dict2
print(chain_map.maps)
print(chain_map.parents)  # 生成一个除第一个dict的其他所有dict的新ChainMap
print(chain_map.new_child())  # 生成一个包含之前的ChainMap的新ChainMap,默认第一个dict为{}
dict3 = {'f': 6}
print(chain_map.new_child(dict3))
