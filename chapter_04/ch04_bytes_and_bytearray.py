# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/3/20 19:55'
# @email = 'fengh@asto-inc.com'
# 知识点：二进制序列的切片始终是同一类型的二进制序列
# 知识点2：bytearray对象的切片还是bytearray对象

# 1、bytes
cafe = bytes('café', encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])

# 2、bytearray
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[:-1])
