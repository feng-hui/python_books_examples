#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/11 16:20
import asyncio
import sys
import itertools


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/|\\'):
        status = char + ' ' + msg
        write(status)
        length = len(status)
        flush()
        write('\x08' * length)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

        write(' ' * length + '\x08' * length)


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner object：', spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    result = asyncio.run(supervisor())
    print('Answer: ', result)


if __name__ == "__main__":
    main()
