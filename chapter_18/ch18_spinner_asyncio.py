#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/2/25 19:28
import asyncio
import sys
import itertools


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/|\\'):
        status = char + ' ' + msg
        write(status)
        length = len(status)
        flush()
        write('\x08' * length)
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

        write(' ' * length + '\x08' * length)


@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 42


@asyncio.coroutine
def supervisor():
    t = asyncio.async(spin('thinking!'))
    print('spinner object：', t)
    result = yield from slow_function()
    t.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer: ', result)


if __name__ == "__main__":
    main()
