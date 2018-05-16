#!/usr/bin/python
# -*- coding: utf-8 -*-


class HauntedBus(object):
    """幽灵校车,原因是因为使用可变参数作为形参"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':

    bus1 = HauntedBus(['Alice', 'Bill'])

    print(bus1.passengers)
    # print(dir(HauntedBus.__init__)

    # pick one passenger named Charlie
    bus1.pick('Charlie')

    # drop one passenger named ALice
    bus1.drop('Bill')

    # another

    bus2 = HauntedBus()

    # bus2 picks one passenger named Carrie

    bus2.pick('Carrie')

    print(bus2.passengers)

    print(HauntedBus.__init__.__defaults__)

    # antoher

    bus3 = HauntedBus()

    # bus3 pick one passenger named Dave

    bus3.pick('Dave')

    print(bus3.passengers)

    print(HauntedBus.__init__.__defaults__)
