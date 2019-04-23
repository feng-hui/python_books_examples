#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/4/23 20:08
from collections import Counter


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
words_count = Counter(words)
print(words_count)
print(words_count['eyes'])

top_three = words_count.most_common(3)  # 统计前三个次数最多的单词
print(top_three)

more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
words_count.update(more_words)
print(words_count)
print(words_count['eyes'])
