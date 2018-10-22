#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-3-24 下午9:41
# @author : Feng_Hui
# @email  : capricorn1203@126.com


class Demo(object):
    """
    the difference of staticmethod and classmethod
    the first argument of classmethhod always is <class '__main__.Demo'>
    """

    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


if __name__ == "__main__":
    print(Demo.klassmeth())
    print(Demo.klassmeth('spam'))
    print(Demo.statmeth('spam'))
