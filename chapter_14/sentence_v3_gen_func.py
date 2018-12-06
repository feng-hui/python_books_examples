#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/6 19:46
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """
    抛弃第二版中的迭代器类SentenceIterator
    第三版 使用生成器函数
    """

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return