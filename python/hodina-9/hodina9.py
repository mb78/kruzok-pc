#!/bin/env python3

from urllib.request import urlopen

with urlopen( 'https://www.whatismypublicip.com/' ) as webpage:
    content = webpage.read()

print( content )
