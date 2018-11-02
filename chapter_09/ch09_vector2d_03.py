#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-02 21:48
# @author : feng_hui
# @email  : capricorn1203@126.com
from array import array
from math import hypot


class Vector2d(object):

    __slots__ = ('__x', '__y')

    type_code = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

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
        return hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(*memv)


