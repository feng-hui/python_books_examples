#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/4/9 13:52
import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)  # 把list转化为heap(堆)

print(heap)  # 打印转化为heap的结果，结果为list

print(heapq.heappop(heap))  # 打印最小的数字
print(heapq.heappop(heap))
print(heapq.heappop(heap))

print(heapq.nlargest(3, heap))  # 打印最大的3个元素,结果为list
print(heapq.nsmallest(3, heap))  # 打印最小的3个元素,结果为list
