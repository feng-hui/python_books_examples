#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-19 20:47
# @author : feng_hui
# @email  : capricorn1203@126.com
import abc


class Tombola(abc.ABC):
    """定义并使用一个抽象基类"""

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素。"""

    @abc.abstractmethod
    def pick(self):
        """
        随机删除元素，然后将其返回。
        如果实例为空，这个方法应该抛出`LookupError`。
        """

    def loaded(self):
        """如果至少有一个元素，返回`True`，否则返回`False`"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素构成。"""
        items = []
        while True:
            try:
                items.pop()
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))