#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/19 14:58
import itertools
import math
import reprlib
from array import array
from functools import reduce
from math import sqrt
import numbers
from operator import xor


class Vector(object):
    """v5 格式化"""
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

    def angle(self, n):
        """
        使用公式把向量的分量数组内的笛卡儿积转换成球面坐标
        可以查看维基百科中的“n纬球体”词条（https://en.wikipedia.org/wiki/N-sphere）
        :param n: index
        :return: 球面坐标
        """
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and self[-1] < 0:
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(','.join(components))
