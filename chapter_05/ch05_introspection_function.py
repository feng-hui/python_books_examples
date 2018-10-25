#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-12 下午11:02
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from inspect import signature
from pprint import pprint


def clip(text: str, max_len: 'int > 0'=80, *, d=3) -> str:
    """
    该函数主要用于截取一段文本
    演示如何获取函数内省相关的值
    :return: 截断后的文本
    """
    end = None
    space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0:
        end = space_before
    else:
        space_after = text.rfind(' ', max_len)
        if space_after:
            end = space_after
    if not end:
        end = len(text)
    return text[:end].rstrip()


def deco(func):
    series = []

    def inner():
        series.append(func.__name__)
        print(series)
        print('running inner()')
    return inner


@deco
def decorated_func():
    print('running deco')


if __name__ == "__main__":

    # 演示函数
    default_text = 'introspection function text'
    clip_text = clip(default_text, max_len=14, d=2)
    print('函数clip的返回值： ', clip_text)

    # 返回函数的注解
    print('返回函数和参数的注解： ', clip.__annotations__)

    # 判断函数是否可调用
    print('判断函数是否可调用: ', clip.__call__)

    # 函数闭包,自由变量的绑定,这里指的是装饰器里的类似series这样的变量
    print('函数闭包中自由变量的绑定： ', decorated_func.__closure__)

    # __code__
    print('编译成字节码的函数元数据和函数定义体: ', clip.__code__)
    print('函数的参数和函数体中的自定义对象: ', clip.__code__.co_varnames)
    print('函数的参数个数(不包含*和**的变长参数): ', clip.__code__.co_argcount)

    # __defaults__
    print('形式参数的默认值： ', clip.__defaults__)

    # __globals__
    print('函数所在模块的全局变量： ')
    pprint(clip.__globals__)

    # __kwdefaults__
    print('仅限关键字形式参数的的默认值： ', clip.__kwdefaults__)

    # __name__
    print('函数名称： ', clip.__name__)

    # __qualname__
    print('函数的限定名称: ', clip.__qualname__)

    # 提取函数的签名
    sig = signature(clip)
    print('函数签名： ', sig)  # 返回函数注解信息

    # 返回参数的种类和默认值
    for name, param in sig.parameters.items():
        print(param.kind, '(参数的种类):', name, '=', param.default, '(参数的默认值,没有默认值返回inspect._empty)')

