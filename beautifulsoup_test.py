import urllib.request, urllib.parse, urllib.error
from icecream import ic
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

names = [(re.findall('known_by_([^ .]*)', url))[0]]
for i in range (count + 1):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = str(tags[position -1].get('href', None)) # type: ignore
    if url is None:
        print("Error: URL not found")
        break
    if i != count:
        names.append(tags[position - 1].contents[0]) # type: ignore

ic(names)
print(names[-1])
