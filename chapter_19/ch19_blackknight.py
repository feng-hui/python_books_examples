#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/17 10:49


class BlackKnight:

    def __init__(self):
        self.members = ['an arm', 'another arm',
                        'a leg', 'another leg']
        self.phrases = ["'Tis but a scratch",
                        "It's just a fles wound.",
                        "I'm invincible.",
                        "All right, we'll call it a draw."]

    @property
    def member(self):
        print("next member is:")
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'BLACK KNIGHT (loses {})\n-- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))

    # def __delattr__(self, item):
    #     text = 'BLACK KNIGHT (loses {})\n-- {}'
    #     print(text.format(self.members.pop(0), self.phrases.pop(0)))


class BlackKnight2:

    def __init__(self):
        self.members = ['an arm', 'another arm',
                        'a leg', 'another leg']
        self.phrases = ["'Tis but a scratch",
                        "It's just a fles wound.",
                        "I'm invincible.",
                        "All right, we'll call it a draw."]

    @property
    def member(self):
        print("next member is:")
        return self.members[0]

    def __delattr__(self, item):
        text = 'BLACK KNIGHT (loses {})\n-- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))


if __name__ == "__main__":
    knight = BlackKnight()
    print(knight.member)
    del knight.member

    knight2 = BlackKnight()
    print(knight2.member)
    del knight2.member
