#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-26 21:08
# @author : feng_hui
# @email  : capricorn1203@126.com


class Avg(object):

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total_num = len(self.series)
        sum_num = sum(self.series)
        return sum_num / total_num


def make_average():
    """closure"""
    series = []

    def averager(new_value):
        series.append(new_value)
        total_num = len(series)
        sum_num = sum(series)
        return sum_num / total_num
    return averager


if __name__ == "__main__":

    # 使用类获取平均值
    print('>>>>>>使用类获取平均值>>>>>>')
    avg = Avg()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    # 使用闭包获取平均值
    print('>>>>>>使用闭包获取平均值>>>>>>')
    avg2 = make_average()
    print(avg2(10))
    print(avg2(11))
    print(avg2(12))
