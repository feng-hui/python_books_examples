#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-2-27 下午7:44
# @author : Feng_Hui
# @email  : capricorn1203@126.com

# 字典推导

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),  # 孟加拉共和国
    (234, 'Nigeria'),  # 尼日利亚
    (7, 'Russia'),
    (81, 'Japan')
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

filter_country = {country.upper(): code for country, code in country_code.items() if code > 66}
print(filter_country)
