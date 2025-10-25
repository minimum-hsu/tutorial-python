#!/usr/bin/env python3

from pathlib import Path
from xml.sax import parse, ContentHandler

class AppleDailyNewsHandler(ContentHandler):

    __title = ''
    __link = ''
    __current_path = ''

    def startElement(self, tag, attrs):
        self.__current_path += '.' + tag

    def endElement(self, tag):
        if tag == 'item':
            print((self.__title, self.__link))
        self.__current_path = self.__current_path[:-len(tag)-1]

    def characters(self, data):
        if self.__current_path.endswith('.item.title'):
            self.__title = data
        elif self.__current_path.endswith('.item.link'):
            self.__link = data

if __name__ == '__main__':
    workdir = Path(__file__).parent
    parse(workdir / 'news.xml', AppleDailyNewsHandler())
