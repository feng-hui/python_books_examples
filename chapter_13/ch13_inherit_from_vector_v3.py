#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/17 19:33
from chapter_10.ch10_vector_v3 import Vector
from itertools import zip_longest


class AnotherVector(Vector):

    def __add__(self, other):
        pairs = zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)

    def __mul__(self, scalar):
        return Vector(n * scalar for n in self)

    def __rmul__(self, scalar):
        return self * scalar


if __name__ == "__main__":
    v1 = AnotherVector([1, 2, 3])
    # print(v1)
    # print(type(v1))
    print(v1 + [1, 2, 3])
    print(v1 * 10)
    print(20 * v1)
