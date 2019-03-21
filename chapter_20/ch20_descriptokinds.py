#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/21 14:36


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo))


class OveRidding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverRiddingNoGet:
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverRidding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:

    over = OveRidding()
    over_no_get = OverRiddingNoGet()
    non_over = NonOverRidding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))
