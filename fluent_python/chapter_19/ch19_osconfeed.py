#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/15 15:25
import os
import json
import warnings
from urllib.request import urlopen


URL = "https://www.oreilly.com/pub/sc/osconfeed"
JSON = "E:\wksp\\fluent_python_examples\chapter_19\data\osconfeed.json"


def load():
    if not os.path.exists(JSON):
        msg = 'download from {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON, encoding='utf-8') as fp:
        return json.load(fp)


if __name__ == "__main__":
    load()
