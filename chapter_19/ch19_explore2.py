#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/15 17:35
from collections import abc
from keyword import iskeyword


class FrozenJSON:
    """
    一个只读接口，使用属性表示法访问JSON类对象
    explore1处理使用<python 关键字>作为属性报错，报错类型为SyntaxError
    """

    def __new__(cls, obj):
        if isinstance(obj, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            # 字典中的键值无法通过该方法获得
            # 类的属性或方法可以
            # 主要使用场景是对象的方法或属性，有则为True，否则为False
            return getattr(self.___data, item)
        else:
            try:
                FrozenJSON(self.__data[item])
            except KeyError:
                raise AttributeError


if __name__ == "__main__":
    fj = FrozenJSON({'name': 'name111', 'class': 'class111'})
    print(fj.name)
