#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2018/12/6 20:01


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


if __name__ == "__main__":
    arithmetic_progression = ArithmeticProgression(1, 2, 5)
    print(list(arithmetic_progression))
    print(list(ArithmeticProgression(0, .1, .5)))
