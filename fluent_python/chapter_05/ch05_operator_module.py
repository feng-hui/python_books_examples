#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-10-25 21:28
# @author : feng_hui
# @email  : capricorn1203@126.com
# how to use operator
from operator import mul, itemgetter, attrgetter, methodcaller
from functools import reduce, partial
from collections import namedtuple
from unicodedata import normalize


def factorial(n):
    """
    :param n: 任意正整数
    :return: n！
    factorial(5) return 5!
    """
    return reduce(lambda a, b: a * b, range(1, n + 1))


def factorial2(n):
    """
    :param n: 任意正整数
    :return: n！
    factorial2(5) return 5!
    """
    return reduce(mul, range(1, n + 1))


if __name__ == "__main__":
    print('use reduce and lambda: ', factorial(5))
    print('use reduce and mul from operator: ', factorial2(5))

    # itemgetter
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print(sorted(metro_data, key=itemgetter(1)))

    # attrgetter
    LatLong = namedtuple('LatLong', 'lat, long')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [
        Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data
    ]
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)
    name_lat = attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))

    # methodcaller
    s = 'The time has come.'
    uppercase = methodcaller('upper')
    print(uppercase(s))

    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s))

    # use partial
    triple = partial(mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 10))))

    nfc = partial(normalize, "NFC")
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1 == s2)
    print(nfc(s1) == nfc(s2))
