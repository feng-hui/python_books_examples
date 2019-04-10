#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/19 20:10
"""
doctest
python -i ch20_method_is_descriptor.py
>>> word = Text('forward')
>>> word
Text'forward'
>>> word.reverse()
Text'drawrof'
>>> Text.reverse(Text('backward'))
Text'drawkcab'
>>> type(Text.reverse), type(word.reverse)
(<class 'function'>, <class 'method'>)
>>> list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')]))
['diaper', (30, 20, 10), Text'desserts']
>>> word.reverse
<bound method Text.reverse of Text'forward'>
>>> Text.reverse.__get__(word)
<bound method Text.reverse of Text'forward'>
>>> Text.reverse.__get__(None, Text)
<function Text.reverse at 0x0000025F3BFC88C8>
>>> word.reverse.__self__
Text'forward'
>>> word.reverse.__func__ is Text.reverse
True
"""
import collections


class Text(collections.UserString):
    """
    method is descriptor
    """

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]
