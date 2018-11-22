#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-22 22:41
# @author : FF
# @email  : capricorn1203@126.com
import sys
from contextlib import contextmanager


@contextmanager
def looking_glass():

    original_write = sys.stdout.write

    def reverse_text(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_text

    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == "__main__":
    with looking_glass() as what:
        print('Alice')
        1/0
        print(what)
    print(what)
