#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-4-29 下午11:35
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from collections import defaultdict
import re


def index_default():
    word_re = re.compile(r'\w+')
    # index = {}
    index = defaultdict(list)
    with open('./files_examples/ch3_default_dict.txt', encoding='utf=-8') as fp:
        for line_no, line in enumerate(fp, 1):
            # print(line)
            for each_word in word_re.finditer(line):
                word = each_word.group()
                line_column = each_word.start() + 1
                location = (line_no, line_column)
                # occurrences = index.get(word, [])
                # print(occurrences)
                # occurrences.append(location)
                index[word].append(location)
        return index


if __name__ == "__main__":
    mapping_index = index_default()
    for each_index in sorted(mapping_index, key=str.upper):
        print(each_index, mapping_index[each_index])
