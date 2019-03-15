#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/15 17:28
from collections import abc


class FrozenJSON:
    """
    一个只读接口，使用属性表示法访问JSON类对象
    explore1处理使用<python 关键字>作为属性报错，报错类型为SyntaxError
    """

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if key.iskeyword():
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
    print(fj.name)
