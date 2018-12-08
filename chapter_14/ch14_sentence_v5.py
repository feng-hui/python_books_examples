#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/6 19:52
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """
    采用生成器表达式替代v4中的for循环【相当于替代列表推导式】
    """

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group for match in RE_WORD.finditer(self.text))
