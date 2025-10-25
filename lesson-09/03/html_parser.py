#!/usr/bin/env python3

from html.parser import HTMLParser
from html.entities import name2codepoint
from pathlib import Path

class MyHTMLParser(HTMLParser):
    __in_tbody = False
    __in_td_th = False
    __in_tr = False
    __print = False

    def handle_starttag(self, tag, attrs):
        if tag == 'tbody':
            self.__in_tbody = True
        elif tag == 'tr':
            self.__in_tr = True
        elif tag in ('td', 'th'):
            self.__in_td_th = True

        for attr in attrs:
            if attr[1] and 'print_hide' in attr[1]:
                self.__print = True

    def handle_endtag(self, tag):
        self.__print = False
        if tag == 'tbody':
            self.__in_tbody = False
        elif tag == 'tr':
            self.__in_tr = False
            if self.__in_tbody:
                print('')
        elif tag in ('td', 'th'):
            self.__in_td_th = False

    def handle_data(self, data):
        if self.__in_tbody and self.__in_td_th:
            data = data.strip()
            if self.__print and data and data not in ('查詢'):
                print(data, end = ',')

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

if __name__ == '__main__':
    workdir = Path(__file__).parent
    myfile = workdir / 'rate.html'
    content = myfile.read_text()

    parser = MyHTMLParser()
    parser.feed(content)
