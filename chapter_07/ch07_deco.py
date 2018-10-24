#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-24 20:25
# @author : feng_hui
# @email  : capricorn1203@126.com


def deco(func):
    def inner():
        print('running inner')
    print(func.__name__)
    return inner


@deco
def target():
    print('running target')


if __name__ == "__main__":
    target()
