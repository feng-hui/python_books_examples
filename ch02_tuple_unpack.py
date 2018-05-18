# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/5/17 14:52'
# @email = 'fengh@asto-inc.com'
# examples 2-8 tuple unpack(元组拆包)
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.20889)),
    ('Mexico City', 'MX', 20.142, (19.4333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'Br', 19.649, (-23.54778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))
