#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-12 下午11:02
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from inspect import signature


def clip(text, max_len=80) -> str:
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


if __name__ == "__main__":

    # 演示函数
    default_text = 'introspection function text'
    clip_text = clip(default_text, max_len=14)
    print(clip_text)

    # 获取函数的默认参数
    print(clip.__defaults__)

    print(clip.__code__)  # 编译成字节码的函数元数据和函数定义体
    print(clip.__code__.co_varnames)  # 函数的参数和函数体中的自定义对象
    print(clip.__code__.co_argcount)  # 函数的参数个数,不包含*和**的变长参数

    # 返回函数的注解
    print(clip.__annotations__)

    # 提取函数的签名
    sig = signature(clip)
    print(sig, type(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
