#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/23 9:15
from ch21_evalsupport import deco_alpha

print('<[1]> evaltime module start')


class ClassOne:

    print('<[2]> ClassOne body')

    def __init__(self):
        print('<[3]> ClassOne.__init__')

    def __del__(self):
        print('<[4]> ClassOne.__del__')

    def method_x(self):
        print('<[5]> ClassOne.method_x')

    class Two(object):
        print('<[6]> ClassTwo body')


@deco_alpha
class ClassThree:
    print('<[7]> ClassThree body')

    @staticmethod
    def method_y():
        print('<[8]> ClassThree.method_y')


class ClassFour(ClassThree):
    print('<[9]> ClassFour body')

    @staticmethod
    def method_y():
        print('<[10]> ClassFour.method_y')


if __name__ == "__main__":
    print('<[11]> ClassOne Tests', 30 * '.')
    one = ClassOne()
    one.method_x()
    print('<[12]> ClassThree Tests', 30 * '.')
    three = ClassThree()
    three.method_y()
    print('<[13]> ClassFour Tests', 30 * '.')
    four = ClassFour()
    four.method_y()

print('<[14]> evaltime module end')
