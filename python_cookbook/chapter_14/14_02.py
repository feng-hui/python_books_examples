#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/6/24 19:13
"""
问题
你写的单元测试中需要给指定的对象打补丁，用来断言它们在测试中的期望行为
（比如，断言被调用时的参数个数，访问指定的属性等）。

解决方案
unittest.mock.patch() 函数可被用来解决这个问题。 patch() 还可被用作一个
装饰器、上下文管理器或单独使用，尽管并不常见。

"""
import unittest
from unittest.mock import patch
import mymodule


with patch('mymodule.func') as mock_func:
    res = mymodule.func(42)
    mock_func.assert_called_with(42)


sample_data = {
        'IBM': 91.1,
        'AA': 13.25,
        'MSFT': 27.72
    }


class Tests(unittest.TestCase):

    @patch('mymodule.dow_prices', return_value=sample_data)
    def test_dow_prices(self, mock_urlopen):
        p = mymodule.dow_prices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT': 27.72}
                         )


if __name__ == "__main__":
    unittest.main()
