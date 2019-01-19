#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/19 16:46
from functools import reduce
from operator import add

from chapter_10.ch10_vector_v3 import Vector
from itertools import zip_longest
import numbers


class AnotherVector(Vector):

    def __add__(self, other):
        # v1
        # pairs = zip_longest(self, other, fillvalue=0.0)
        # return Vector(a + b for a, b in pairs)
        # v2
        try:
            pairs = zip_longest(self, other, fillvalue=0.0)
            return AnotherVector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        # v1
        # return Vector(n * scalar for n in self)

        # v2
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        pairs = zip_longest(self, other, fillvalue=0.0)

        # v1
        # return reduce(add, (a * b for a, b in pairs))

        # v2
        try:
            return sum((a * b for a, b in pairs))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented


if __name__ == "__main__":
    va = AnotherVector([1, 2, 3])
    vb = AnotherVector(range(1, 4))
    print(va == vb)

    # 判断等值的元组与Vector对象是否相等
    t3 = (1, 2, 3)
    print(va == t3)

    # 判断Vector2d对象实例与Vector对象实例是否相等
    # 在判断类型之后，解释器会通过调用Vector2d的__eq__方法来判定，所以结果仍然为True
    from chapter_09.ch09_vector2d_03 import Vector2d
    vc = Vector2d(1, 2)
    vd = AnotherVector([1, 2])
    print(vd == vc)
