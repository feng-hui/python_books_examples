#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/18 19:14


class Quantity:
    """
    descriptor 描述符类
    """
    _counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls._counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls._counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    """
    托管类
    自动获取存储属性的名称
    """

    weight = Quantity()  # 描述符实例 weight
    price = Quantity()  # 描述符实例price

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    coconuts = LineItem('Brazilian coconut', 20, 17.95)
    print(coconuts.weight, coconuts.price)
    print(coconuts.subtotal())
