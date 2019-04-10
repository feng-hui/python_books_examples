#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn12032126.com
# @time: 2019/1/2 21:32
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    """
    子生成器
    :return: 返回平均值
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def grouper(results, key):
    """
    委派生成器
    :param results: 结果字典
    :param key: 字典的key
    :return: 获取自生成器的值返回给调用方
    """
    while True:
        results[key] = yield from averager()


def main(data: dict):
    """
    调用方,接收传入的参数字典,通过委派生成器中的yield from表达式对子生成器进行直接操作
    :param data:
    :return:
    """
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    # print(results)
    report(results)


def report(results: dict):
    """
    生成结果
    :param results: 结果字典
    :return: 打印结果
    """
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit
        ))


if __name__ == "__main__":
    data_dt = {
        'girls;kg':
            [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m':
            [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg':
            [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m':
            [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
    }
    main(data_dt)
