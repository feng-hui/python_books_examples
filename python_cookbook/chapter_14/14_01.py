#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/6/10 19:55
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import mymodule


class TestUrlPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.url_print(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)


if __name__ == "__main__":
    TestUrlPrint().test_url_gets_to_stdout()
