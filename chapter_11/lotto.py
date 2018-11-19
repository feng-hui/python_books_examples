#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-19 21:08
# @author : feng_hui
# @email  : capricorn1203@126.com
import random
from chapter_11.tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, items):
        self._balls = list(items)

    def load(self, items):
        self._balls.extend(items)

    def pick(self):
        try:
            random.randrange(self._balls)
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop()

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
