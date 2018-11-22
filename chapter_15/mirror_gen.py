#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-22 22:23
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

    yield 'JABBERWOCKY'

    sys.stdout.write = original_write


if __name__ == "__main__":
    with looking_glass() as what:
        print('Alice')
        print(what)
    print(what)
