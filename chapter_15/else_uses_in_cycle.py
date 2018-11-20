#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-20 22:09
# @author : feng_hui
# @email  : capricorn1203@126.com
import collections


# 1.for...else... and try...else...
try:
    my_list = []
    for item in my_list:
        if item.suit == 'banana':
            break
    else:
        print('running else from for cycle')
        # raise ValueError('No Banana flavor found!')
except ValueError:
    pass
else:
    print('running else from try')

# 2.while...else...
i = 1
while i < 5:
    # if i == 3:
    #     break
    i += 1
else:
    print('running else from while cycle')
