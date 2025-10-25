#!/usr/bin/env python3

from pathlib import Path
from xml.dom.minidom import parse

def parse_appledaily_news(file_: str):
    dom = parse(file_)
    root = dom.documentElement
    items = [x for x in root.getElementsByTagName('channel')[0].childNodes \
        if x.nodeType is root.ELEMENT_NODE and x.nodeName == 'item']

    ###################################
    # sub function
    ###################################
    def parse_item(item):
        for node in item.childNodes:
            if node.nodeName == 'title':
                title = parse_title(node)
            elif node.nodeName == 'link':
                link = parse_link(node)
        return title, link

    def parse_title(node) -> str:
        return parse_data(node)

    def parse_link(node) -> str:
        return parse_data(node)

    def parse_data(node) -> str:
        for n in node.childNodes:
            if n.nodeType in (root.TEXT_NODE, root.CDATA_SECTION_NODE):
                return n.data
    # end of sub function

    news = [parse_item(item) for item in items]
    return news

if __name__ == '__main__':
    workdir = Path(__file__).parent
    news = parse_appledaily_news(str(workdir / 'news.xml'))
    print(*news, sep = '\n')
