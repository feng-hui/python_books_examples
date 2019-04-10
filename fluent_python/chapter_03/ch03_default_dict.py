#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-4-29 下午11:35
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from collections import defaultdict
import re


def set_default1():
    """how to use dict"""
    word_re = re.compile(r'\w+')
    index = {}
    with open('./files_examples/ch3_default_dict.txt', encoding='utf=-8') as fp:
        for line_no, line in enumerate(fp, 1):
            # print(line)
            for each_word in word_re.finditer(line):
                word = each_word.group()
                line_column = each_word.start() + 1
                location = (line_no, line_column)
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences
        return index


def set_default2():
    """how to use setdefault in dict"""
    word_re = re.compile(r'\w+')
    index = {}
    with open('./files_examples/ch3_default_dict.txt', encoding='utf=-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for each_word in word_re.finditer(line):
                word = each_word.group()
                line_column = each_word.start() + 1
                location = (line_no, line_column)
                index.setdefault(word, []).append(location)
        return index


def set_default3():
    """
    how to use defaultset
    可以通过default方法初始化一个dict,默认值为empty list
    """
    word_re = re.compile(r'\w+')
    index = defaultdict(list)
    with open('./files_examples/ch3_default_dict.txt', encoding='utf=-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for each_word in word_re.finditer(line):
                word = each_word.group()
                line_column = each_word.start() + 1
                location = (line_no, line_column)
                index[word].append(location)
        return index
    

if __name__ == "__main__":

    # don't use setdefault
    print(">>>>>>01 don't use setdefault>>>>>>\n")
    mapping_index = set_default1()
    for each_index in sorted(mapping_index, key=str.upper):
        print(each_index, mapping_index[each_index])

    # use setdefault
    print('>>>>>>>02 how to use setdefault>>>>>>\n')
    mapping_index = set_default2()
    for each_index in sorted(mapping_index, key=str.upper):
        print(each_index, mapping_index[each_index])

    # [recommended]use defaultset
    print('>>>>>>>02 how to use defaultset>>>>>>\n')
    mapping_index = set_default3()
    for each_index in sorted(mapping_index, key=str.upper):
        print(each_index, mapping_index[each_index])
