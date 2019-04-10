#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-9 下午8:19
# @author : Feng_Hui
# @email  : capricorn1203@126.com
import collections


class StrKeyDict0(dict):
    """
    example 3-7
    exchange non-str key to str key when querying
    """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        """key in dict will be called"""
        return item in self.keys() or str(item) in self.keys()


class StrKeyDict2(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        """different from the example of 3-8"""
        pass

    def __setitem__(self, key, value):
        """different from the example of 3-8"""
        pass


str_key_dict = StrKeyDict0([('a', 2), ('b', 3), (4, 'c')])
print('a' in str_key_dict)
