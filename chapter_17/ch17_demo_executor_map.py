#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/22 18:44
from time import strftime, sleep
from concurrent import futures


def display(*args):
    print(strftime('[%HH:%MM:%SS]'), end='\n')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10


def main():

    # with futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     results = executor.map(loiter, range(5))

    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results: ', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))


if __name__ == "__main__":
    main()
