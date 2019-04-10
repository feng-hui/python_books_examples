#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-05 22:11
# @author : feng hui
# @email  : capricorn1203@126.com
import reprlib
from array import array
from math import sqrt


class Vector(object):

    type_code = 'd'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __iter__(self):
        return iter(self._components)

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
        return tuple(self) == tuple(other)

    def __abs__(self):
        return sqrt(sum(x * x for x in self._components))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(memv)
