#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-12-03 21:44
# @author : FH
# @email  : capricorn1203@126.com
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """
    采用生成器函数替代v2中的【迭代器】类
    """

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    """迭代器"""

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self
