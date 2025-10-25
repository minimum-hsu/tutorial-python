#!/usr/bin/env python3

import logging
import os
from pathlib import Path
import unittest
from urllib import request
from xml_parser_et import parse_xml as parse

class NewsTestCase(unittest.TestCase):
    workdir = Path(__file__).parent
    report = workdir / 'report.log'
    xml = workdir / 'example.xml'

    def setUp(self):
        logging.basicConfig(
            format = '%(asctime)s [%(levelname)s] %(message)s',
            datefmt = '%Y-%m-%dT%H:%M:%S%z',
            level = logging.INFO,
            filename = self.report
        )

        self.url = 'https://status.aws.amazon.com/rss/billingconsole.rss'

        # download news xml
        with request.urlopen(self.url) as rss:
            data = rss.read().decode('utf-8')

        with open(self.xml, 'w') as f:
            f.write(data)

    def tearDown(self):
        logging.info('[success] %s', self.url)

    def doCleanups(self):
        # os.remove(self.xml)
        pass

    def test_parse(self):
        self.assertIsInstance(parse(self.xml), list)

if __name__ == '__main__':
    unittest.main()
