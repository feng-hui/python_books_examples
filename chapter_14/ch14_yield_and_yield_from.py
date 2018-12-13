#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/13 19:15


def chain(*iterable):
    """the function is like `itertools.chain`"""
    for it in iterable:
        for i in it:
            yield i


def chain2(*iterable):
    """use `yield from`"""
    for it in iterable:
        yield from it


if __name__ == "__main__":
    it1 = 'ABC'
    it2 = tuple(range(3))
    print(list(chain(it1, it2)))
    print(list(chain2(it1, it2)))
