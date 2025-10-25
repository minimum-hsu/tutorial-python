#!/usr/bin/env python3

from pathlib import Path
import xml.etree.ElementTree as ET

def parse_xml(file_: str):
    tree = ET.parse(file_)
    root = tree.getroot()

    news = [(item.find('title').text, item.find('link').text) for item in root.iter('item')]
    return news

if __name__ == '__main__':
    workdir = Path(__file__).parent
    news = parse_xml(workdir / 'example.xml')
    print(*news, sep = '\n')
