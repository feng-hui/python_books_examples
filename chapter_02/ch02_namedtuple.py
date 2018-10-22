#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

City = namedtuple('City', 'name country population coordatinates')

tokyo = City('Tokyo', 'Japan', 36.933, (35.689722, 139.691667))

print(tokyo, type(tokyo), tokyo.name)

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.20889))

delhi = City._make(delhi_data)

delhi_dict = delhi._asdict()

print(delhi)

print(delhi_dict, type(delhi_dict))