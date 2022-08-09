# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
repeats = int(input('Enter amounts of repeats: '))
position = int(input('Enter position: '))

'''
Initially tried while loop method for this

while placeholder < repeats:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    placeholder = 0

    for tag in tags:
        placeholder += 1

        if placeholder > position:
            break
        url = tag.get('href', None)
        print('Retrieving: ', url)
'''

for x in range(repeats):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    placeholder = 0

    for tag in tags:
        placeholder += 1

        if placeholder > position:
            break
        url = tag.get('href', None)
        print('Retrieving: ', url)

print(url)

