#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/6 19:49
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """
    采用finditer替代findall
    更惰性地实现可迭代
    """

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            return match.group()
