#!/usr/bin/python
# -*- coding: utf-8 -*-


def bubble_sort(list1):
    """冒泡排序"""
    length = len(list1)
    for n in range(1, length):
        for i in range(length - n):
            left = list1[i]
            right = list1[i + 1]
            if left < right:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
    return list1


if __name__ == "__main__":
    my_list = [1, 34, 56, -2, 3, 57]
    print(bubble_sort(my_list))
