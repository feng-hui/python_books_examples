#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/1 17:40
from .a import A


class B(A):

    @staticmethod
    def bar():
        print(B.bar)
