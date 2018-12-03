#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-12-03 20:59
# @author : FH
# @email  : capricorn1203@126.com
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
