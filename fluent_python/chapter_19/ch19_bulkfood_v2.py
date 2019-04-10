#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/17 9:14


class LineItem:
    """
    使用特性(@property)验证属性weight是否大于0
    """

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError('value must be > 0')


if __name__ == "__main__":
    line_item = LineItem('d', 20, 10)
    print(line_item.__class__)
    print(line_item.__dict__)
