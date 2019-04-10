#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 2018-11-24 22:46
# @author : FH
# @email  : capricorn1203@126.com
import doctest
from chapter_11.tombola import Tombola
from chapter_11 import bingo, lotto, tombolist


TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests {1.failed:2} failed {2}'


def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    virtual_subclasses = list(Tombola._abc_registry)
    for cls in real_subclasses + virtual_subclasses:
        example_test(cls, verbose)


def example_test(cls, verbose=False):

    res = doctest.testfile(
        filename=TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == "__main__":
    import sys
    main(sys.argv)
