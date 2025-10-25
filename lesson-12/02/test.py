#!/usr/bin/env python3

import unittest
from xml_parser_et import parse_appledaily_news as parse
from urllib import request
import logging
import os


class NewsTestCase(unittest.TestCase):
    report = 'report.log'
    xml = 'news.xml'

    def setUp(self):
        logging.basicConfig(
            format = '%(asctime)s [%(levelname)s] %(message)s',
            datefmt = '%Y-%m-%dT%H:%M:%S%z',
            level = logging.INFO,
            filename = self.report
        )

        self.news_url = 'https://tw.appledaily.com/rss/newcreate/kind/rnews/type/106'

        # download news xml
        with request.urlopen(self.news_url) as rss:
            data = rss.read().decode('utf-8')

        with open(self.xml, 'w') as f:
            f.write(data)

    def tearDown(self):
        logging.info('[success] %s', self.news_url)

    def doCleanups(self):
        os.remove(self.xml)

    def test_parse(self):
        self.assertIsInstance(parse(self.xml), list)


if __name__ == '__main__':
    unittest.main()
