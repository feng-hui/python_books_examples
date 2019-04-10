#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-24 20:35
# @author : feng_hui
# @email  : capricorn1203@126.com
registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
