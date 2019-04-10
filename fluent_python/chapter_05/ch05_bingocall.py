#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-11 下午8:58
# @author : Feng_Hui
# @email  : capricorn1203@126.com
import random


class BingoCall(object):
    """
    演示如何让一个类可以实现函数的功能
    只要在类中定义__call__函数就可以自定义一个可调用的类
    """

    def __init__(self, items):
        self._item = list(items)
        random.shuffle(self._item)

    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == "__main__":

    bingo = BingoCall(range(10000))
    print(callable(bingo))
    print(bingo.pick())
    print(bingo())
    print(bingo())
    # print(bingo())
