#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/19 20:10
import collections


class Text(collections.UserString):

    def __repr__(self):
        return 'Text{!r}'.format(self.data)

    def reverse(self):
        return self[::-1]