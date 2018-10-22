#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-2-26 下午9:06
# @author : Feng_Hui
# @email  : capricorn1203@126.com


def partition(v, left, right):
    """
    获取经过一轮排序后基准值的位置

    快排原理介绍：假设序列为[6, 8, 1, 4, 3, 9]
    默认基准数为6,从右向左进行扫描,找到第一个比6小的数字为3,交换6和3的位置;
    然后从左向右进行扫描,找到第一个比6大的数字为8,然后交换6和8的位置,然后返回最后基准数停留的位置
    重复上述过程,直到基准数左边的数字都比基准数小,基准数右边的数字都比基准数大
    """
    key = v[left]
    low = left
    high = right
    while low < high:
        while low < high and v[high] >= key:
            high -= 1
        v[low] = v[high]
        while low < high and v[low] <= key:
            low += 1
        v[high] = v[low]
        v[low] = key
    return low


def quick_sort(v, left, right):
    """快速排序"""
    if left < right:
        position = partition(v, left, right)
        quick_sort(v, left, position - 1)
        quick_sort(v, position + 1, right)
    return v


if __name__ == "__main__":
    s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
    begin = 0
    end = len(s) - 1
    print(quick_sort(s, begin, end))
