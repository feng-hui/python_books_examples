#!/usr/bin/python
# -*- coding: utf-8 -*-

from array import array
from random import random

floats = array('d', (random() for i in xrange(10 ** 7)))

print(floats[-1])

# save the last number to file

fp = open('floats.bin', 'wb')

floats.tofile(fp)

fp.close()

# read from file floats.bin

floats2 = array('d')

fp = open('floats.bin', 'rb')

floats2.fromfile(fp, 10**7)

fp.close()

print(floats2[-1])



