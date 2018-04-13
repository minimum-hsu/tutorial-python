#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def parse_appledaily_news(file_: str):
    tree = ET.parse(file_)
    root = tree.getroot()

    news = [(item.find('title').text, item.find('link').text) for item in root.iter('item')]
    return news


if __name__ == '__main__':
    news = parse_appledaily_news('news.xml')
    print(*news, sep = '\n')

