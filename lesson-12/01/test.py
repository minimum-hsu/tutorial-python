#!/usr/bin/env python3

import unittest
from timestamp import parse_timestamp as parse


class TimestampTestCase(unittest.TestCase):

    def test_iso8601(self):
        self.assertIsNotNone(parse('2018-04-13T09:39:21'))
        self.assertIsNotNone(parse('2018-04-13T09:39:21.578'))
        self.assertIsNotNone(parse('2018-04-13T09:39:21+0800'))

    def test_slash(self):
        self.assertIsNotNone(parse('2018/04/13 09:39:21'))

    def test_special(self):
        self.assertIsNotNone(parse('Fri Apr 13 09:39:21 UTC 2018'))


if __name__ == '__main__':
    unittest.main()
        
