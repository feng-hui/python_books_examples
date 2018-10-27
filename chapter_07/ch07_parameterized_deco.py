#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-27 15:55
# @author : feng_hui
# @email  : capricorn1203@126.com


registry = set()


def register(active=False):
    def decorator(func):
        print('running register (active=%s) -> decorate(%s)'
              % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorator


@register()
def f1():
    print('running f1()')


@register(active=True)
def f2():
    print('running f2()')


def f3():
    print('running f3()')


if __name__ == "__main__":
    f1()
    f2()
    f3()