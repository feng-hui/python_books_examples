#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-3-4 下午10:33
# @author : Feng_Hui
# @email  : capricorn1203@126.com
import tkinter


def print_mro(cls):
    print(cls.__mro__, type(cls.__mro__))
    print(','.join(c.__name__ for c in cls.__mro__))


if __name__ == "__main__":
    print_mro(bool)
    print_mro(tkinter.Text)
