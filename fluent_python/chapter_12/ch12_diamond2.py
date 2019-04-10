#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-3-4 下午10:24
# @author : Feng_Hui
# @email  : capricorn1203@126.com


class A:
    """菱形继承问题"""
    def ping(self):
        print('ping in A: ', self)


class B(A):
    def pong(self):
        print('pong in B: ', self)


class C(A):
    def pong(self):
        print('PONG in C:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping in D: ', self)

    def pingpong(self):
        A.ping(self)  # 直接调用超类A的ping方法
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)
