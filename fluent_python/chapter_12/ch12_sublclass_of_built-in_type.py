#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-3-4 下午9:39
# @author : Feng_Hui
# @email  : capricorn1203@126.com


class DoppelDict(dict):
    """
    子类化内置类型[不建议使用]
    内置类型不会调用子类覆盖覆盖的方位
    """
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == "__main__":
    dd = DoppelDict(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)
