#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/24 21:11
from functools import wraps


def coroutine(func):
    """
    预激协程装饰器
    wraps装饰器把相关的属性从func复制到被它装饰的函数里
    wraps里是一个partial函数【见5.10.2】
    partial函数用于部分应用于一个函数。部分应用是指，基于一个函数创建一个新的可调用对象，
    把原函数的某些参数固定。
    使用这个函数可以把一个或多个参数的函数改编成需要回调的API。
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer
