#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import hypot


class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __abs__(self):
		return hypot(self.x, self.y)

	def __repr__(self):
		return 'Vecotr(%r, %r)' %(self.x, self.y)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self, scalar):
		x = self.x * scalar
		y = self.y * scalar
		return Vector(x, y)

	def __bool__(self):
		print(abs(self))
		return bool(abs(self))


if __name__ == '__main__':
	vector = Vector(3, 4)
	vector2 = Vector(9, 16)
	print(vector)
	print(abs(vector))
	print(vector + vector2)
	print(vector2 * 3)
	print(bool(vector))