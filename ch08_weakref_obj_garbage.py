#!/usr/bin/python
# -*- coding: utf-8 -*-

import weakref


def bye():
    print('Gone with the wind...')


if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = s1

    # register callable named bye on s1 object
    ender = weakref.finalize(s1, bye)

    # check the attribute of alive
    print(ender.alive)

    # delete s1
    del s1

    # check the attribute of alive again
    print(ender.alive)

    # s2 = "spam"
    s2 = "spam"

    # check again
    print(ender.alive)
