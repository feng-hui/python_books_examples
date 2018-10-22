#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-2-26 下午3:03
# @author : Feng_Hui
# @email  : capricorn1203@126.com
import weakref


class Cheese(object):
    """定义一个Cheese类"""
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == "__main__":
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    # print(sorted(stock.items()))
    print(sorted(stock.keys()))
    del catalog
    # 删除catalog之后,stock并不为空???
    print(sorted(stock.keys()))
    # 原因是:cheese这个局部变量引用了对象导致了变量的存在时间比预期长
    del cheese
    print(sorted(stock.keys()))

