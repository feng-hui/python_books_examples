#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import deque

dq = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

print(dq)

dq.rotate(3)

print(dq)

dq.rotate(4)

print(dq)

dq.appendleft(-1)

print(dq)

dq.extend([11, 22, 33])

print(dq)

dq.extendleft([10, 20, 30, 40])

print(dq)