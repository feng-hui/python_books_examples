#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-01 21:09
# @author : feng_hui
# @email  : capricorn1203@126.com
from array import array
from math import hypot


class Vector2d(object):

    type_code = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (
            bytes([ord(self.type_code)]) + bytes(array(self.type_code, self))
        )

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(*memv)


if __name__ == "__main__":

    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(v1)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(bytes(v1))
    print(v1.from_bytes(bytes(v1)))
