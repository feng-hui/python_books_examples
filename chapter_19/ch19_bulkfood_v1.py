#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/17 9:09


class LineItem:
    """
    使用特性验证属性1
    当前类无法验证实例属性，比如weight或price是正负值
    如果是在超市消费或其他消费的情况下，则这两个值必须都大于0
    """

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
