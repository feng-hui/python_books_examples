#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/17 19:33
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
            return Vector(a + b for a, b in pairs)
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


if __name__ == "__main__":
    v1 = AnotherVector([1, 2, 3])

    # add
    print('>>>>>>1、You will test the method of addition.')
    print(v1 + [1, 2, 3])
    print([1, 2, 3] + v1)
    # print(v1 + 1)
    # print(v1 + 'ABC')

    # mul
    print('>>>>>>2、You will test the method of multiplication.')
    print(v1 * 10)
    print(20 * v1)
    print(v1 * True)

    # matrix multiplication
    print('>>>>>>3、You will test the method of matrix multiplication.')
    v2 = AnotherVector([1, 2, 3])
    v3 = AnotherVector([5, 6, 7])
    print(v2 @ v3)
    print([20, 30, 40] @ v2)
