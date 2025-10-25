#!/usr/bin/env python3

from html.parser import HTMLParser
from html.entities import name2codepoint
from pathlib import Path

class MyHTMLParser(HTMLParser):
    candidate = [
        '.tbody.tr.td',
        '.tbody.tr.td.div.div'
    ]
    __current_path = ''
    __print = False

    def handle_starttag(self, tag, attrs):
        self.__current_path += '.' + tag
        for attr in attrs:
            if attr[1] and 'print_hide' in attr[1]:
                self.__print = True

    def handle_endtag(self, tag):
        self.__print = False
        if self.__current_path.endswith('.tbody.tr'):
            print('')
        self.__current_path = self.__current_path[:-len(tag)-1]

    def handle_data(self, data):
        for template in self.candidate:
            if self.__current_path.endswith(template):
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
