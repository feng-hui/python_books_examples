#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/5/11 18:11
"""
1.20 合并多个字典或映射

问题
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，比如查找值或者检查某些键是否存在。

解决方法：
使用 collections 模块中的 ChainMap 类。

总结:

1、一个ChainMap接受多个字典并将它们再逻辑上变为一个字典。然而，这些字典并不是真的合并在一起了，而是在内部
创建了一个容纳这些字典的列表并重新定义了一些常见的字典操作来便利这个列表。
2、如果出现重复键，那么第一次出现的应设置会被返回。
3、对于字典的更新或删除操作总是影响的是列表中的第一个字典。
4、ChainMap对于变成语言中的作用范围变量（不如globals， locals等）是非常有用的。
5、可以通过update()方法将两个字典合并，但是这样操作的话如果源自点更新的话，这种改变不会反应到新的合并字典中去。
"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])  # 从a中高输出
print(c['z'])  # 从b中输出

# 更新或删除
c['z'] = 10
c['w'] = 40
print('更新了z和w键之后: ', c)
del c['x']
print('删除了c中的x之后: ', c)

# 想删除第一个序列中不存在的键y
try:
    del c['y']
except KeyError:
    print('因为第一个序列中没有y，所以无法删除')

# 测试总结中的第4点
values = ChainMap()
values['x'] = 1
values = values.new_child()  # 添加一个新的字典
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)

# 测试通过update()方法来合并字典
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print('通过update方法合并后的字典为: ', merged)
a['x'] = 13
print('更改了a中x的值之后，合并后的字典为: ', merged)
