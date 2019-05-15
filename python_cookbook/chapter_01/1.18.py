#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/5/11 17:49
"""
一、主要内容

# 映射名称到序列元素
# namedtuple（具名元组）的使用
# 具名元组的实例看起来是一个普通的类实例，但是它跟元组类型是可交换的，支持所有的普通元组操作，比如索引和解压

命名元组的用途:
1、将你的代码从下标操作中解脱出来
2、作为字典的替代，字典存储需要更多的内存空间。如果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会
更加高效。但是需要注意的是，一个命名元组是无法进行修改的。
"""
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['address', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 按照属性进行访问
print(sub.address, sub.joined)

# 打印具名元组实例的长度
print(len(sub))

# 使用元组拆包功能
address, joined = sub
print(address, joined)

# 由于命名元组无法修改
# 所以修改命名元组，需要使用命名元组实例的_replace()方法
# _replace()方法还有一个很游泳的特性就是当你的命名元组拥有可选或者缺失字段时候，它是一个非常方便的填充数据的方法。可以
# 先创建一个包含缺省值，然后使用该方法创建新的值来更新实例。
sub_modified = sub._replace(joined='2019-05-11')
print(sub_modified)
