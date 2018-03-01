#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-2-27 上午12:35
# @author : Feng_Hui
# @email  : capricorn1203@126.com


def straight_selection_sort(l):
    """直接选择排序"""
    count = len(l)
    for i in range(0, count):
        min_index = i
        for j in range(i + 1, count):
            if l[min_index] > l[j]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]
    return l


if __name__ == "__main__":
    my_list = [1, 34, 56, -2, 3, 57]
    print(straight_selection_sort(my_list))
