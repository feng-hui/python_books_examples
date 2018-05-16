#!/usr/bin/python
# -*- coding: utf-8 -*-


class TwilightBus(object):
    """让乘客消失的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    basketball_team = ['Alice', 'Bill', 'Claire', 'David']
    bus1 = TwilightBus(basketball_team)
    bus1.drop('Alice')
    bus1.drop('David')
    print(basketball_team)
