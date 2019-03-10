#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/1 20:12
import time
from tqdm import tqdm


for i in tqdm(range(100)):
    print(i)
    time.sleep(.01)
