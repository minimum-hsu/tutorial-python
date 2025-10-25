#!/usr/bin/env python3

import requests

def fetch_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code != 200:
        raise Exception('Failed to fetch URL: {}'.format(url))
    return response.text

if __name__ == '__main__':
    url = 'http://www.google.com'
    content = fetch_url(url)
    print(content)
