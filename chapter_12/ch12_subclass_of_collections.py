#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-3-4 下午9:53
# @author : Feng_Hui
# @email  : capricorn1203@126.com
import collections


class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == "__main__":
    dd = DoppelDict2(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)
