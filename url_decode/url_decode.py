#!/usr/bin/env python3

import sys
import urllib

print("Its not working,
seehttps://stackoverflow.com/questions/47916737/ipython-import-and-python-import-are-different ")

def decode_url(url):
    return urllib.parse.unquote(url)



if len(sys.argv) >= 2:
    print(decode_url(sys.argv[1]))
else:
    print("""Usage:
    url_decode.py <url_2_decode>
    """)
