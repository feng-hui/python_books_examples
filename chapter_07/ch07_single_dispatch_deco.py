#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-27 11:23
# @author : feng_hui
# @email  : capricorn1203@126.com
import html
from functools import singledispatch
from numbers import Integral
from collections.abc import MutableSequence


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text.replace('\n', '<br> \n'))
    return '<p>{0}</p>'.format(content)


@htmlize.register(Integral)
def _(n):
    return '<pre>{0}(0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == "__main__":
    """
    demand:
    1. str  把内部的换行符替换为'<br> \n',不使用<pre>,而是使用<p>;
    2. int  以十进制和十六进制显示数字；
    3. list 输出一个html列表,根据各个元素的类型进行格式化
    
    use：singledispatch 单分派泛函数的使用
    """
    print(htmlize({1, 2, 3}))
    print(htmlize('single dispatch'))
    print(htmlize(123))
    print(htmlize(['123', '456', '789']))

