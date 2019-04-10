#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-25 22:12
# @author : feng_hui
# @email  : capricorn1203@126.com
from unicodedata import name, normalize


ohm = '\u2126'  # Ω
print(ohm)
print(name(ohm), end='\n\n')

# NFC是W3C推荐的规范化形式之一
# 使用NFC规范的时候,单个字符会被规范成另外一个单字符
ohm_c = normalize("NFC", ohm)
print(ohm_c)
print(name(ohm_c), end='\n\n')

print(ohm == ohm_c)
print(normalize("NFC", ohm) == normalize("NFC", ohm_c))
