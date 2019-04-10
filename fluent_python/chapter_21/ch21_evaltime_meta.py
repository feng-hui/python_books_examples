#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/23 9:49
from ch21_evalsupport import deco_alpha, MetaAleph

print('<[1]> evaltime module start')


@deco_alpha
class ClassThree:
    print('<[2]> ClassThree body')

    @staticmethod
    def method_y():
        print('<[3]> ClassThree.method_y')


class ClassFour(ClassThree):
    print('<[4]> ClassFour body')

    @staticmethod
    def method_y():
        print('<[5]> ClassFour.method_y')


class ClassFive(metaclass=MetaAleph):
    print('<[6]> ClassFive body')

    def __init__(self):
        print('<[7]> ClassFive.__init__')

    @staticmethod
    def method_z():
        print('<[8]> ClassFive.method_z')


class ClassSix(ClassFive):
    print('<[9]> ClassSix body')

    @staticmethod
    def method_z():
        print('<[10]> ClassSix.method_z')


if __name__ == "__main__":
    print('<[11]> ClassThree Tests', 30 * '.')
    three = ClassThree()
    three.method_y()
    print('<[12]> ClassFour Tests', 30 * '.')
    four = ClassFour()
    four.method_y()
    print('<[13]> ClassFive Tests', 30 * '.')
    five = ClassFive()
    five.method_z()
    print('<[14]> ClassSix Tests', 30 * '.')
    six = ClassSix()
    six.method_z()

print('<[15]> evaltime module end')
