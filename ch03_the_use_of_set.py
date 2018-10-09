#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-10-9 下午9:19
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from unicodedata import name

# setcomps 集合推导
set_comps = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(set_comps)

set_comps2 = {name(chr(i), '') for i in range(32, 256)}
print(set_comps2)