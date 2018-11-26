#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-22 21:16
# @author : FF
# @email  : capricorn1203@126.com
import sys


class LookingGlass:

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_text
        return 'JABBERWOCKY'

    def reverse_text(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


if __name__ == "__main__":
    with LookingGlass() as what:
        print('Alice')
        print(what)
