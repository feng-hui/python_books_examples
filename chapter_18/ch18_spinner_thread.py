#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/2/2 15:08
import time
import threading
import sys
import itertools


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/|\\'):
        status = char + ' ' + msg
        write(status)
        length = len(status)
        flush()
        write('\x08' * length)
        if not signal.go:
            break
        write(' ' * length + '\x08' * length)


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    t = threading.Thread(target=spin, args=(
        'Thinking!', signal
    ))
    t.start()
    print('spinner object：', t)
    result = slow_function()
    signal.go = False
    t.join()
    return result


if __name__ == "__main__":
    res = supervisor()
    print('Answer: ', res)
