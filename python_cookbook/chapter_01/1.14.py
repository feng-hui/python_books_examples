#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/4/30 19:36
# 排序不支持原生比较的对象
# attrgetter的使用
from operator import attrgetter


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


if __name__ == "__main__":
    users = [User(30), User(6), User(23)]

    # sort method1
    print(sorted(users, key=lambda r: r.user_id))

    # sort method2, faster than method1
    print(sorted(users, key=attrgetter('user_id')))

    # get the maximum user id
    print(max(users, key=attrgetter('user_id')))

    # get the minimum user id
    print(min(users, key=attrgetter('user_id')))
