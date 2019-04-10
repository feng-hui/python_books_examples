# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/4/28 16:52'
# @email = 'fengh@asto-inc.com'
import re
WORD_RE = re.compile(r'\w+')


def word_mapping():
    """
    创建一个单词到其出现情况的映射
    使用setdefault
    """
    index = {}
    with open('./files_examples/ch3_word_mapping.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            # print(line_no, line)
            for match in WORD_RE.finditer(line):
                # print(match, match.start())
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)
    return index


if __name__ == "__main__":
    mapping_index = word_mapping()
    # print(mapping_index)
    for each_word in sorted(mapping_index, key=str.upper, reverse=True):
        print(each_word, mapping_index[each_word])
