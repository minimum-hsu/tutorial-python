#!/usr/bin/env python3

from urllib import request

def fetch_url(url: str) -> str:
    with request.urlopen(url) as response:
        return response.read().decode('utf-8')

if __name__ == '__main__':
    url = 'http://www.google.com'
    content = fetch_url(url)
    print(content)
