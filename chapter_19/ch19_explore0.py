#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/15 16:16
from collections import abc


class FrozenJSON:
    """
    一个只读接口，使用属性表示法访问JSON类对象
    FrozenJson只有一个__init__方法和一个实例属性__data
    当访问其他属性时，会调用__getattr__方法报错
    所以这个类并不会打印json的键值
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            # 字典中的键值无法通过该方法获得
            # 类的属性或方法可以
            # 主要使用场景是对象的方法或属性，有则为True，否则为False
            return getattr(self.___data, item)
        else:
            try:
                FrozenJSON.build(self.__data[item])
            except KeyError:
                raise AttributeError

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == "__main__":
    fj = FrozenJSON({'name': 'name111', 'class': 'class111'})
    print(fj.name2)
