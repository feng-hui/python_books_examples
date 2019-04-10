#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-19 21:15
# @author : feng_hui
# @email  : capricorn1203@126.com
import random
from chapter_11.tombola import Tombola


@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == "__main__":
    print(issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print(isinstance(t, Tombola))
    print(TomboList.__mro__)
