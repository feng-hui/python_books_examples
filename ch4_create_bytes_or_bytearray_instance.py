# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/3/21 19:44'
# @email = 'fengh@asto-inc.com'
# 1、str对象+encoding参数
bytes_instance = bytes('café', encoding='utf-8')
print('the instance of bytes with utf-8 encoding: {}'.format(bytes_instance))

bytes_instance = bytes('café', encoding='gbk')
print('the instance of bytes with gbk encoding: {}'.format(bytes_instance))

# 2、一个可迭代对象，提供0~255之间的数值
bytes_instance = bytes([0, 3, 233])
print('the instance of bytes with an iterable object: {}'.format(bytes_instance))

# 3、通过实现缓冲协议对象的实例进行构建(后续了解实现缓冲协议对象)
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print('the instance of bytes with the instance created by an array object: {}'.format(octets))
