#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/23 11:42
import ch21_model_v8 as model


class LineItem(model.Entity):
    """
    托管类,自动获取存储属性的名称
    entity为定制描述符类的装饰器
    """
    description = model.NonBlank()  # 描述符实例
    weight = model.Quantity()  # 描述符实例
    price = model.Quantity()  # 描述符实例

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
