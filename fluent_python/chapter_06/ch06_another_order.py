#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-19 下午9:43
# @author : Feng_Hui
# @email  : capricorn1203@126.com
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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Customer Name: {} Order; total: {:.2f}; due: {:.2f}>'
        return fmt.format(self.customer.name, self.total(), self.due())


def fidelity_promo(order):
    """
    积分超过1000折扣5%
    """
    return order.total() * .05 if order.customer.fidelity > 1000 else 0


def bulk_item_promo(order):
    """单个商品超过20个或以上时折扣10%"""
    dis_count = 0
    for item in order.cart:
        if item.quantity > 20:
            dis_count += order.total() * .1
    return dis_count


def large_order_promo(order):
    """商品总数超过10个或以上时折扣7%"""
    distinct_item = {item.product for item in order.cart}
    total_quantities = len(distinct_item)
    if total_quantities >= 10:
        return order.total() * .07
    else:
        return 0


# 获取最好的折扣
promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    return max(promo(order) for promo in promos)


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
    order1 = Order(joe, order_cart, fidelity_promo)
    print(order1)

    another_order_1 = Order(joe, order_cart, best_promo)
    print(another_order_1)

    order2 = Order(ann, order_cart, fidelity_promo)
    print(order2)

    order3 = Order(ann, order_cart2, bulk_item_promo)
    print(order3)

    order4 = Order(ann, order_cart3, large_order_promo)
    print(order4)
