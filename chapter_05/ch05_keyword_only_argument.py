#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-12 下午9:51
# @author : Feng_Hui
# @email  : capricorn1203@126.com


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个html"""
    if cls:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(['%s="%s"' % (attr_key, attr_value)
                            for attr_key, attr_value in attrs.items()])
    else:
        attr_str = ''

    if content:
        html = '\n'.join(['<%s %s>%s<%s>' %
                          (name, attr_str, each_content, name) for each_content in content])
    else:
        html = '<%s %s />' % (name, attr_str)
    return html


def f(a, *, b):
    """
    传入类似b=2的仅限关键字参数(keyword-only argument)
    参数不能写为(a, *b),可以在对应的关键字参数加*,
    如这个函数所写则必须传入参数b,而f2函数则不用传入b参数,而且返回的b的值也是有区别的
    """
    return a, b


def f2(a, *b):
    return a, b


if __name__ == "__main__":

    custom_html_br = tag('br')
    print(custom_html_br)

    custom_html_img = tag('img', src='http://**.img.com/image_1.jpg')
    print(custom_html_img)

    custom_html_p = tag('p', 'hello', 'world', cls="custom_p")
    print(custom_html_p)

    custom_html_dict = tag(**{'name': 'img', 'src': 'http://**.img.com/image_1.jpg'})
    print(custom_html_dict)

    print(f(1, b=2))
    print(f2(1, 2))
    print(f2(1, 2))
    print(dir(f2))
