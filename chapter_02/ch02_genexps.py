#!/usr/bin/python
# -*- coding: utf-8 -*-

import array

symbols = '##$$^&*()'

genexps = tuple(ord(s) for s in symbols)

my_array = array.array('I', (ord(s) for s in symbols))

print(genexps)

print(my_array)