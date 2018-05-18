# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/5/17 14:45'
# @email = 'fengh@asto-inc.com'
from math import hypot


class Vector(object):
    """
    向量的操作
    """

    def __init__(self, x=0, y=0):
        print(u"调用了__init__")
        self.x = x
        self.y = y

    def __repr__(self):
        """
        控制repr()作用在其实例上时的行为;
        当需要显示一个对象在屏幕上的时候,将这个对象的属性或方法整理成一个可以打印输出的格式
        与eval()对应,把repr()打印输出的结果赋值给eval，可以获得原来的对象类型
        参考：https://www.cnblogs.com/dengyg200891/p/4872751.html
        :return:
        """
        print(u"调用了__repr__")
        return 'Vector(%r, %r)' % (self.x, self.y)

    # def __str__(self):
    #     print(u"调用了__str__"
    #     return 'Vector(%s, %s)' % (self.x, self.y)

    def __add__(self, other):
        print(u"调用了__add__")
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __bool__(self):
        print(u"调用了__bool__")
        return bool(abs(self))


if __name__ == "__main__":

    # 1.2.1、内置向量类complex
    v1 = complex(1, 2)
    v2 = complex(3, 4)
    v = v1 + v2
    print(v)

    # vector object
    vector1 = Vector(3, 4)
    vector2 = Vector(1, 2)
    vector3 = vector1 + vector2
    vector4 = vector1 * 3
    b = repr(vector1)
    print('--------------------------------')
    print(b, type(eval(b)))
    print('--------------------------------')
    print(vector3, type(vector3))
    print('--------------------------------')
    print(vector4)
    print('--------------------------------')
    print(vector1.__bool__())
    print('--------------------------------')
    print(abs(vector1))
