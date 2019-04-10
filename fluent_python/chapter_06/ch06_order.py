#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-18 下午8:39
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from abc import ABC
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order(object):

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.__total = 0

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if not self.promotion:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Customer Name: {} Order; total: {:.2f}; due: {:.2f}>'
        return fmt.format(self.customer.name, self.total(), self.due())


class Promotion(ABC):

    @staticmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):
    """
    积分超过1000折扣5%
    """

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity > 1000 else 0


class BulkItemPromo(Promotion):
    """单个商品超过20个或以上时折扣10%"""

    def discount(self, order):
        dis_count = 0
        for item in order.cart:
            if item.quantity > 20:
                dis_count += order.total() * .1
        return dis_count


class LargeOrderPromo(Promotion):
    """商品总数超过10个或以上时折扣7%"""

    def discount(self, order):
        distinct_item = {item.product for item in order.cart}
        total_quantities = len(distinct_item)
        if total_quantities >= 10:
            return order.total() * .07
        else:
            return 0


if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    order_cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)
    ]
    order_cart2 = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5)
    ]
    order_cart3 = [
        LineItem(str(item_code), 1, 1.0) for item_code in range(10)
    ]
    order1 = Order(joe, order_cart, FidelityPromo())
    print(order1)

    order2 = Order(ann, order_cart, FidelityPromo())
    print(order2)

    order3 = Order(ann, order_cart2, BulkItemPromo())
    print(order3)

    order4 = Order(ann, order_cart3, LargeOrderPromo())
    print(order4)
