#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

colors = ['black', 'white']

sizes = ['S', 'M', 'L']

# listcomps

start_time1 = time.time()

for tshirt in [(c, s) for c in colors for s in sizes]:
	print(tshirt)
print('listcomps cost time: {}'.format(str(time.time() - start_time1)))

# genexps

start_time2 = time.time()

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
	print(tshirt)
print('genexps cost time: {}'.format(str(time.time() - start_time2)))