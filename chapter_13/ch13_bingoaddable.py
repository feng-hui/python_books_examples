#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/19 17:35
from chapter_11.tombola import Tombola
from chapter_11.bingo import BingoCage


class AddableBingoCage(BingoCage):
    """实现加法和就地加法"""

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            iterable_other = other.inspect()
        else:
            try:
                iterable_other = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = 'right operand in += must be {!r} or an iterable'
                raise TypeError(msg.format(self_cls))
        self.load(iterable_other)
        return self


if __name__ == "__main__":
    vowels = 'AEIOU'

    globe = AddableBingoCage(vowels)
    print(globe.inspect())

    # test __add__
    globe2 = AddableBingoCage('XYZ')
    globe3 = globe + globe2
    print(len(globe3.inspect()))

    # test __iadd__
    globe_orig = globe
    print(len(globe.inspect()))
    globe += ['M', 'N']
    print(len(globe.inspect()))
    print(globe is globe_orig)
