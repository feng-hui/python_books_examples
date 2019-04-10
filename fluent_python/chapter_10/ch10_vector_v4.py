#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/19 14:32
import reprlib
from array import array
from functools import reduce
from math import sqrt
import numbers
from operator import xor


class Vector(object):
    """散列和快速等值测试"""
    type_code = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __iter__(self):
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_names.find(item)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        return AttributeError(msg.format(cls, item))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can't set attribute 'a' to 'z' in {attr_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)

    def __repr__(self):
        """
        string
        :return: if len(string) > 30, return string[:13] + '...' + string[14:]
        """
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (
                bytes([ord(self.type_code)]) + bytes(self._components)
        )

    def __eq__(self, other):

        # v1 适合vector2d
        # return tuple(self) == tuple(other)

        # v2 分量较多的情况下使用
        # if len(self) != len(other):
        #     return False
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True
        #
        # v3更加简单的写法
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        # v1
        # hashes = (hash(x) for x in self._components)
        # return reduce(xor, hashes, 0)
        # v2
        hashes = map(hash, self._components)
        return reduce(xor, hashes, 0)

    def __abs__(self):
        return sqrt(sum(x * x for x in self._components))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(memv)
