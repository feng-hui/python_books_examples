#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-8 下午8:56
# @author : Feng_Hui
# @email  : capricorn1203@126.com


class CustomDict(dict):
    """
    how to use the magic method of __missing__?
    when the dict cannot find a value of a key,then the method will be called.
    """

    def __missing__(self, key):
        print(">>>>>>>the method of __missing__ is called>>>>>>>")
        default_key = None
        return default_key


if __name__ == "__main__":
    custom_dict = CustomDict()
    default_value = custom_dict['a']
    print(default_value)
